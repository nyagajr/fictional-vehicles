from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    cars = CarDetails.objects.all()
    return render(request,'index.html', locals())
