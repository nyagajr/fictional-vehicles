from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CarDetails(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    car_make = models.CharField(max_length =30)
    car_model = models.CharField(max_length =30)
    year = models.CharField(max_length = 30)
    front_image = models.ImageField(upload_to = 'images/', blank=True, null=True)
    rear_image = models.ImageField(upload_to = 'images/', blank=True, null=True)
    logo_image = models.ImageField(upload_to = 'images/', blank=True, null=True)
    dash_image = models.ImageField(upload_to = 'images/', blank=True, null=True)
    def __str__(self):
        return self.car_make
