from django.contrib import admin
from .models import Appointment, Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Appointment)
class AppointmentAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('name', 'created_on', 'approved')
    list_filter  = ('approved', 'created_on')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)

