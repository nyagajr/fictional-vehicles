from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # url(r'^profile/$',views.profile, name='profile'),
]
