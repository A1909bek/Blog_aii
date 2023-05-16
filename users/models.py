from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='images')

    def __str__(self):
        return self.username
    