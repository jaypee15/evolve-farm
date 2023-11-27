from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    email =  models.EmailField(max_length=100)
    phone_number = models.CharField(null=True, blank=True, max_length=100)