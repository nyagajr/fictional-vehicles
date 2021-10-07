from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import CarDetailsForm

def index(request):
    form = CarDetailsForm()

    if request.method == 'POST':
        form = CarDetailsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'index.html', context)
