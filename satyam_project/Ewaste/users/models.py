from django.db import models
from django.contrib.auth.models import AbstractUser




# Create your models here.

class User(AbstractUser):
    is_citizen = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return str(self.user)