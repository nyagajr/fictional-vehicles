from django.db import models

# Create your models here.
class CarDetails(models.Model):
    car_make = models.CharField(max_length =30)
    car_model = models.CharField(max_length =30)
    year = models.CharField(max_length = 30)
    front_image = models.ImageField(upload_to = 'images/', blank=True)
    rear_image = models.ImageField(upload_to = 'images/', blank=True)
    side_image = models.ImageField(upload_to = 'images/', blank=True)
    interior_image = models.ImageField(upload_to = 'images/', blank=True)
    # post = models.CharField(max_length =30)
    def __str__(self):
        return self.car_make
