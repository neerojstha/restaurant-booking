from django.contrib import admin
from .models import Appointment, Review, Menu
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Appointment)
class AppointmentAdmin(SummernoteModelAdmin):

    summernote_fields = ('comments')


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
    



