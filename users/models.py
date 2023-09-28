from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
import datetime


class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("Username is required")

        if not email:
            raise ValueError("Email is required")

        user = self.model(
            username=username,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser should have is_staff set to True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser should have is_superuser set to True")

        return self.create_user(username=username, email=email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=100, verbose_name="Username", null=False, blank=False)

    email = models.CharField(
        max_length=255, verbose_name="Email Address", null=False, blank=False, unique=True)

    profile_image = CloudinaryField(format="jpg", folder="AdminProfileImages", verbose_name="Admin Profile Image", null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    # Define custom related names for the groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group', related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_user_set', blank=True)

    objects = UserManager()

    def save(self, *args, **kwargs):
        # Convert email to lowercase
        self.email = self.email.lower()

        # Capitalize username
        self.username = self.username.capitalize()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
