from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('', views.loginPage, name='login'),
    path('logout/', views.loginPage, name='logout'),

    path('display',views.display, name='display'),
    path('home', views.index, name='home'),
    path('update/<str:pk>/',views.updateDisplay, name='update'),


]
