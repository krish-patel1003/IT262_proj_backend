from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import SymptomSerializer
from .models import Symptom, Prescription, Appointment
from rest_framework.permissions import IsAuthenticated
from .permissions import SymptomPermission
# Create your views here.

class appointmentsHome(GenericAPIView):
    
    def get(self, request):
        return Response({"Appointments home"})


class SymptomViewSet(ModelViewSet):

    serializer_class = SymptomSerializer
    queryset = Symptom.objects.all()
    permission_classes = (IsAuthenticated, SymptomPermission, )


