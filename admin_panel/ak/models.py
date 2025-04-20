from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from .manager import GFGUserManager



class GFG(AbstractUser):
    username = None  # Remove username
    phone = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = GFGUserManager()

    def __str__(self):
        return self.phone
