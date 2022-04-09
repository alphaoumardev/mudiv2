from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# from mart.models import Product


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("The user must have an email")
        if not username:
            raise ValueError("The user must have an username ")
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class CustomerProfile(AbstractUser):
    SEX = (("Male", "Male"),
        ("Female", "Female"),
        ("Secret", "Secret"),)

    email = models.EmailField(verbose_name="email", max_length=40, unique=True, null=True)
    username = models.CharField(max_length=20, unique=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True, null=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True, null=True)

    phone_number = models.CharField(max_length=15, unique=True, null=True)
    avatar = models.ImageField(upload_to="mudi", null=True, blank=True)
    country = models.CharField(max_length=10, default="China")
    gender = models.CharField(max_length=10, null=True, choices=SEX)
    email_verified = models.BooleanField(default=False, )

    state_or_province = models.CharField(max_length=20, default="Jiangsu",)
    city = models.CharField(max_length=20, default="Najing",)
    zip_code = models.IntegerField(default=210010)
    detailed_address = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)




    # def user_name(self):
    #     return self.user.username + '   (' + self.user.email + ')    ' + self.user.first_name
    #
    # def avatar_preview(self):
    #     if self.avatar:
    #         return mark_safe(f'<img src="{self.avatar.url}" style="width: 50px; height:50px; object-fit:contain;" />')
    #     else:
    #         return 'No avatar'

    # avatar_preview.short_description = "Avatar"
