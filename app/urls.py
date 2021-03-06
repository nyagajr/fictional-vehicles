from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('',views.landing, name='landing'),
    path('user/', views.userPage, name='user'),
    path('display',views.display, name='display'),
    path('home', views.index, name='home'),
    path('update/<str:pk>/',views.updateDisplay, name='update'),
    path('demo/', views.display_demo, name='demo'),


]
