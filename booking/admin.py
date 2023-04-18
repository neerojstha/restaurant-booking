from django.contrib import admin
from .models import Post, Guest, Appointment, Review, Menu, Cancellation, Table
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    pass

@admin.register(Appointment)
class AppointmentAdmin(SummernoteModelAdmin):
    pass


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    pass


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_filter  = ('name', 'price')
    search_fields = ('name', 'description')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'rating', 'created_at')
    list_filter  = ('name', 'created_at')
    search_fields = ('name', 'email', 'body')
    

@admin.register(Cancellation)
class CancellationAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'reason')
    list_filter = ('date', 'email')
    search_fields = ('reason', 'email')

