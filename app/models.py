from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,  PermissionsMixin
from django.contrib.auth.password_validation import validate_password
from uuid import uuid4


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff=False, is_superuser=False, **other_fields):
        if not email:
            raise ValueError('Email address must be specified')

        if not password:
            raise ValueError('Password must be specified')

        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_superuser=is_superuser,
            **other_fields
        )

        validate_password(password)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, **other_fields):
        return self._create_user(email, password, False, False, **other_fields)

    def create_superuser(self, email, password, **other_fields):
        return self._create_user(email, password, True, True, **other_fields)

    def has_perm(self, user_obj, perm, obj=None):
        return user_obj.is_staff

    def has_module_perms(self, user_obj, app_label):
        return user_obj.is_staff


class ProfileUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=254, unique=True)    
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    date_of_birth = models.DateField()

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['first_name', 'username', 'date_of_birth']
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"