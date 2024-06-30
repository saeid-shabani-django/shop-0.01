from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    age = models.PositiveIntegerField(null=True,blank=True)


