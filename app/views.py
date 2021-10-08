from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import CarDetailsForm

def display(request):
    cars = CarDetails.objects.all()

    form = CarDetailsForm()

    if request.method == 'POST':
        form = CarDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request,'test.html',locals())

def updateDisplay(request, pk):
    instance = get_object_or_404(CarDetails, id=pk)
    form = CarDetailsForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'test.html', {'form': form})

def index(request):
    cars = CarDetails.objects.all()
    return render(request,'index.html',locals())
