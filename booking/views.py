from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from .models import Post, Guest, Appointment, Review, Menu, Cancellation



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'about.html'


def appointment(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'appointment.html')

def menu(request):
    items = Menu.objects.all()
    return render(request, 'menu.html', {'items': items})

def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'guest_list.html', {'guests': guests})

def guest_detail(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    return render(request, 'guest_detail.html', {'guest': guest})

def guest_new(request):
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            guest = form.save()
            return redirect('guest_detail', pk=guest.pk)
    else:
        form = GuestForm()
    return render(request, 'guest_edit.html', {'form': form})
