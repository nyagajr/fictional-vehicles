from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CarDetailsForm

def display(request):

    form = CarDetailsForm()

    if request.method == 'POST':
        form = CarDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    cars = CarDetails.objects.all()
    return render(request,'test.html',locals())

def index(request):
    cars = CarDetails.objects.all()
    return render(request,'index.html',locals())
