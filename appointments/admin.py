from django.contrib import admin
from .models import Symptom, Prescription, Appointment
# Register your models here.

admin.site.register(Symptom)
admin.site.register(Prescription)
admin.site.register(Appointment)