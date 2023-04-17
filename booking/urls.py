from . import views
from django.urls import path

urlppatterns = [
    path('', views.Appointment.as_view(), name='home')
    ]