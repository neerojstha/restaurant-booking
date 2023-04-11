from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Guest, Appointment, Review, Menu, Cancellations


