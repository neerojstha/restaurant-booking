from . import views
from .views import appointment, menu
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('appointment/', views.appointment, name='appointment'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.appointment, name='appointment'),
    
]

