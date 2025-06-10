from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUser(AbstractUser, UserManager):
    identifier = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'identifier'

    def __str__(self):
        return self.username
