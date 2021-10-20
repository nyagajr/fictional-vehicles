from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from django.forms import ModelForm
from .models import *

class CarDetailsForm(ModelForm):
    class Meta:
        model = CarDetails
        fields = ['car_make','car_model','year','front_image','rear_image','logo_image','dash_image']

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
