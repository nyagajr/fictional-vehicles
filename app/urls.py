from django.urls import path

from . import views

urlpatterns = [
    path('display',views.display, name='display'),
    path('index', views.index, name='index'),

]
