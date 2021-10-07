from django.forms import ModelForm
from .models import CarDetails

class CarDetailsForm(ModelForm):
    class Meta:
        model = CarDetails
        fields = '__all__'
