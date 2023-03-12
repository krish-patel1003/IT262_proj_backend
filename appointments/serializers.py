from rest_framework.serializers import ModelSerializer
from .models import Symptom, Prescription, Appointment
from users.models import StudentProfile


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
        extra_kwargs = {
            "student":{"read_only":True}
        }

    def create(self, attrs):
        student = StudentProfile.objects.get(user=self.context["request"].user)
        attrs["student"] = student
        prescription = Prescription.objects.create()
        attrs['prescription_id'] = prescription
        super().validate(attrs)

        return super().create(attrs)
