from rest_framework.serializers import ModelSerializer
from .models import Symptom, Prescription, Appointment


class SymptomSerializer(ModelSerializer):

    class Meta:
        model = Symptom
        fields = ("id", "name", "is_verified")