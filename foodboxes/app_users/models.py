from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
