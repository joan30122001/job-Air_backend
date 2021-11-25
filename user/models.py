from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pseudo = models.CharField(max_length=50),
    email = models.EmailField(max_length=254),
    password = models.CharField(max_length=50)
    