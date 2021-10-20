from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    prof_pic = models.ImageField(upload_to = 'images/', blank=True, null=True)
    bio = models.CharField(max_length = 50)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'


class CarDetails(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    car_make = models.CharField(max_length =30)
    car_model = models.CharField(max_length =30)
    year = models.CharField(max_length = 30)
    front_image = models.ImageField(upload_to = 'images/', blank=True, null=True)
    rear_image = models.ImageField(upload_to = 'images/', blank=True, null=True)
    logo_image = models.ImageField(upload_to = 'images/', blank=True, null=True)
    dash_image = models.ImageField(upload_to = 'images/', blank=True, null=True)
    def __str__(self):
        return self.car_make
