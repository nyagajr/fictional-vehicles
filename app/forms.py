from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from django.forms import ModelForm
from .models import *

class CarDetailsForm(ModelForm):
    class Meta:
        model = CarDetails
        fields = '__all__'

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
