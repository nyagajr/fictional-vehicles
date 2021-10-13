from django.urls import path
from . import views

urlpatterns = [
    path('/',views.display, name='display'),
    path('home', views.index, name='home'),
    path('update/<str:pk>/',views.updateDisplay, name='update'),


]
