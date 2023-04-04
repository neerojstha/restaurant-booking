from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_detail = models.CharField(max_length=50)


class Table(models.Model):
    table_number = models.IntegerField(unique=true)
    table_limit = models.IntegerField()


class Appointment(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.IntegerField()
    number_of_people = models.IntegerField()
    table_number = models.IntegerField()

    def __str__(self):
        return f"{self.guest_name} at table {self.table_number}

    def remove(self):
        clash_Appointment = Apointment.objects.filter(
            table = self.table,
            start_time=self.end_time,
            end_time=self.start_time
        ).exclude(pk=self.pk)

        if clash_Appointment.exists():
            raise ValidationError('This table is already bookind for this time')





class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    comments = models.TextField(null=True, blank=True)
    rating = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CouponCode(models.Model):
    name = models.CharField(max_length=255)
    discount_amount = models.PositiveIntegerField(default=10)
    validity_period_start = models.DateField()
    validity_period_end = models.DateField()



