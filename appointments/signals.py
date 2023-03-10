from django.dispatch import Signal
from django.dispatch import receiver
from .signals import *

appointment_attended = Signal()


@receiver(appointment_attended)
def notify_next_patient(sender, **kwargs):
    print("notify next patient", kwargs)