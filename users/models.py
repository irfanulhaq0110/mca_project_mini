from django.db import models
from django.contrib.auth .models import User
# Create your models here.

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile',on_delete=models.CASCADE)
    phone_no = models.IntegerField(max_length=10)
    is_driver = models.BooleanField(default=False)

class Driverprofile(models.Model):
    vehicle_no = models.CharField(max_length=250)
    license_no = models.CharField(max_length=250)
