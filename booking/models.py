from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))

class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_detail = models.CharField(max_length=55)

  


class Appointment(models.Model):
    name = models.CharField(max_length=255, verbose_name='Appointment Name')
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.IntegerField()
    number_of_people = models.IntegerField()
    table_number = models.IntegerField()
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    table_limit = models.IntegerField()


class Review(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    comments = models.TextField(null=True, blank=True)
    rating = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CouponCode(models.Model):
    name = models.CharField(max_length=255)
    discount_amount = models.PositiveIntegerField(default=10)
    validity_period_start = models.DateField()
    validity_period_end = models.DateField()



