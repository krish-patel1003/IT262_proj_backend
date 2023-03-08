from rest_framework.serializers import ModelSerializer
from .models import Symptom, Prescription, Appointment


class SymptomSerializer(ModelSerializer):

    class Meta:
        model = Symptom
        fields = ("id", "name", "is_verified")

class PrescriptionSerializer(ModelSerializer):

    class Meta:
        model = Prescription
        fields = ("id", "prescription")

class AppointmentSerializer(ModelSerializer):

    class Meta:
        model = Appointment
        fields = (
            "id",
            "student",
            "date", 
            "symptoms", 
            "extra_symptoms", 
            "diagnose", 
            "prescription_id", 
            "status"
        )
        # extra_kwargs = {
        #     "student":{"read_only":True},
        #     "prescription_id":{"read_only":True}
        # }
