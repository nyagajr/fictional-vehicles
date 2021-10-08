from django.urls import path

from . import views

urlpatterns = [
    path('display',views.display, name='display'),
    path('update/<str:pk>/',views.updateDisplay, name='update'),
    path('index', views.index, name='index'),

]
