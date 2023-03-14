from django.dispatch import Signal
from django.dispatch import receiver
from .signals import *

emergency_leave = Signal()


@receiver(emergency_leave)
def reschedule_appointment(sender, **kwargs):
    print("Reschedule Appointments", kwargs)