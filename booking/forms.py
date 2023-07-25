# forms.py
from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'date', 'time', 'number_of_people', 'comments']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'min': '08:00', 'max': '18:00', 'pattern': '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$'}),
        }
