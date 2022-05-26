import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

from mudi import settings


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.is_active = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


SEX = (("Male", "Male"),
       ("Female", "Female"),
       ("Secret", "Secret"),)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=25, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True, null=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True, null=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    avatar = models.ImageField(upload_to="mudi", null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, choices=SEX)
    email_verified = models.BooleanField(default=False, )

#
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def user_profile_receiver(sender, instance=None, created=False, *args, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#
#
# post_save.connect(user_profile_receiver, sender=settings.AUTH_USER_MODEL)
