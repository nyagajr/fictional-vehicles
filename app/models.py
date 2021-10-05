from django.db import models

# Create your models here.
class CarDetails(models.Model):
    car_make = models.CharField(max_length =30)
    car_moddel = models.CharField(max_length =30)
    year = models.CharField(max_length = 30)
    # pic = models.ImageField(upload_to = 'articles/')
    # post = models.CharField(max_length =30)
    def __str__(self):
        return self.car_make
