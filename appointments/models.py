from django.db import models
from users.models import User, StudentProfile
from django.db.models import CheckConstraint, Q, F
from datetime import datetime, timedelta, date
# Create your models here.

class Symptom(models.Model):

    name = models.CharField(max_length=255, unique=True, null=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Prescription(models.Model):

    prescription = models.TextField(null=True)

    def __str__(self):
        return self.id

class Appointment(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Attended', 'Attended')
    ]

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    date = models.DateField()
    symptoms = models.ManyToManyField(Symptom, related_name='symptoms')
    extra_symptoms = models.TextField()
    diagnose = models.TextField(blank=True)
    prescription_id = models.ForeignKey(Prescription,  null=True, on_delete=models.SET_NULL)
    status =  models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')


    class Meta:
        ordering = ('id',)
        constraints = [
            CheckConstraint(
                check =  Q(date__lte = (datetime.now() + timedelta(days=14)).date()),
                name = 'check_appointment_date_range'
            ),
        ]
    
    def __str__(self):
        return f'{self.student.rollno} {self.date}'