import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserAccountManager(BaseUserManager):

    def create_user(self, email, password):

        if not email:
            raise ValueError('Email address is required!')

        email = self.normalize_email(email)
        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        if not email:
            raise ValueError('Email address is required!')

        email = self.normalize_email(email)
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser):

    email = models.EmailField(unique=True, primary_key=True)
    api_key = models.UUIDField(default=uuid.uuid4, editable=False)
    daily_limit = models.IntegerField(default=1000)

    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True