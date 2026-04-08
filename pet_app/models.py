from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    vaccination_date = models.DateField()
    medical_notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    reason = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.pet.name} - {self.appointment_date}"