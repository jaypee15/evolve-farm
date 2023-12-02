from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, blank=False, null=False)
    email =  models.EmailField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=100, blank=False, null=False, default="0000")