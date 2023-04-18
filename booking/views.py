from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from .models import Post, Guest, Appointment, Review, Menu, Cancellation



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

def appointment(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'appointment.html')

def menu(request):
    items = Menu.objects.all()
    return render(request, 'menu.html', {'items': items})


