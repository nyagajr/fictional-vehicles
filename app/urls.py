from django.urls import path
from . import views

urlpatterns = [
    path('',views.display, name='display'),
    path('update/<str:pk>/',views.updateDisplay, name='update'),
    path('home', views.index, name='index'),

]
