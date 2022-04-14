from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

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


class UserAccount(AbstractBaseUser, PermissionsMixin):
    SEX = (("Male", "Male"),
           ("Female", "Female"),
           ("Secret", "Secret"),)

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=False)
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

    state_or_province = models.CharField(max_length=20, default="Jiangsu", )
    city = models.CharField(max_length=20, default="Najing", )
    zip_code = models.IntegerField(default=210010)
    detailed_address = models.TextField(null=True, blank=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email
