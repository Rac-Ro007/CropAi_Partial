from django.urls import path
from . import views

urlpatterns = [
    path('',views.plant_lib, name='plant_lib'),
]
