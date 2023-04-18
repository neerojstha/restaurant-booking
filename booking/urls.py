from . import views
from .views import appointment, menu
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('appointment/', appointment, name='appointment'),
    path('menu/', menu, name='menu'),
    ]

