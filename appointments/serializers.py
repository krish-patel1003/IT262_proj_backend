from rest_framework.serializers import ModelSerializer
from .models import Symptom, Prescription, Appointment
from users.models import StudentProfile
from rest_framework import serializers


class SymptomSerializer(ModelSerializer):

    class Meta:
        model = Symptom
        fields = ("id", "name", "is_verified")

class PrescriptionSerializer(ModelSerializer):

    class Meta:
        model = Prescription
        fields = ("id", "prescription")

class AppointmentSerializer(ModelSerializer):

    # student_data = serializers.SerializerMethodField("get_student_data")

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
            "student":{"read_only":True},
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        student_id = instance.student.id
        student_data = StudentProfile.objects.get(id=student_id)
        name = student_data.user.get_full_name()
        representation["student_data"] = {
            "name": name,
            "rollno": student_data.rollno
        }
        symptoms_list = self.generate_sypmtom_list(instance.id)
        # print(symptoms_list)
        representation["symptoms"] = symptoms_list
        # representation["sypmtoms"] = self.generate_sypmtom_list(instance.id)

        return representation
    def create(self, attrs):
        student = StudentProfile.objects.get(user=self.context["request"].user)
        attrs["student"] = student
        super().validate(attrs)

        return super().create(attrs)

    def generate_sypmtom_list(self, appointment_id):
        appointment = Appointment.objects.get(id=appointment_id)
        symptoms_qs = appointment.symptoms.all()
        # print("symptoms", symptoms_qs)
        symptoms = list(map(lambda i: i.name, symptoms_qs))
        # print(symptoms)
        return symptoms
        # return ["test"]

