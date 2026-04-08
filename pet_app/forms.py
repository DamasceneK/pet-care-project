from django import forms
from .models import Pet, Appointment

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'age', 'vaccination_date', 'medical_notes']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['pet', 'appointment_date', 'reason']