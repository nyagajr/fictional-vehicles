from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user


from .models import *
from .forms import *
from django.contrib import messages

@unauthenticated_user
def registerPage(request):
    form = createUserForm()

    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account for '+ user + ' created!')
            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Incorrect username/password')
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def userPage(request):
    context = {}
    return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
def display(request):
    cars = CarDetails.objects.all()

    form = CarDetailsForm()

    if request.method == 'POST':
        form = CarDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'test.html',locals())

@login_required(login_url='login')
def updateDisplay(request, pk):
    instance = get_object_or_404(CarDetails, id=pk)
    form = CarDetailsForm(request.POST or None,request.FILES, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'test.html', {'form': form})

@login_required(login_url='login')
def index(request):
    cars = CarDetails.objects.all()
    return render(request,'index.html',locals())

def landing(request):
    return render(request, 'landing.html')
