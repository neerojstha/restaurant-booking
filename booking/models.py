from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))

class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_detail = models.CharField(max_length=55)
    address = models.CharField(max_length=210, null=True, blank=True)

  


class Appointment(models.Model):
    name = models.CharField(max_length=255, verbose_name='Appointment Name', null=True, blank=True)
    date = models.DateField()
    time = models.IntegerField()
    number_of_people = models.IntegerField()
    table_number = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    table_limit = models.IntegerField()

class Menu(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Review(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    rating = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


class Cancellation(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    reason = models.CharField(max_length=200)
    date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} - {self.reason}"
    


 