from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.index, name='home'),
    path('home/state', views.filter_districts, name='state'),
    path('home/state/district', views.filter_crops, name='state district'),
]
