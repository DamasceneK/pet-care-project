from django.shortcuts import render, redirect
from .models import Pet, Appointment
from .forms import PetForm, AppointmentForm


def home(request):
    pets = Pet.objects.all()
    appointments = Appointment.objects.all()
    return render(request, 'pet_app/home.html', {
        'pets': pets,
        'appointments': appointments
    })


def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PetForm()

    return render(request, 'pet_app/add_pet.html', {'form': form})


def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppointmentForm()

    return render(request, 'pet_app/add_appointment.html', {'form': form})
def home(request):
    pets = Pet.objects.all()
    appointments = Appointment.objects.all()

    # 👇 collections requirement
    summary = {
        'total_pets': len(pets),
        'total_appointments': len(appointments)
    }

    pet_names = [pet.name for pet in pets]  # list example

    return render(request, 'pet_app/home.html', {
        'pets': pets,
        'appointments': appointments,
        'summary': summary,
        'pet_names': pet_names
    })