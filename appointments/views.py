from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import (
    SymptomSerializer, 
    AppointmentSerializer, 
    PrescriptionSerializer
)
from .models import (
    Symptom, 
    Prescription, 
    Appointment
)
from rest_framework.permissions import IsAuthenticated
from .permissions import (
    SymptomPermission, 
    AppointmentPremission,
    PrescriptionPermission 
)
from rest_framework import status
from users.models import StudentProfile
from django.db.models import Q
from .signals import appointment_attended
from datetime import datetime
from rest_framework.decorators import action
from backend.settings import APPOINTMENT_SETTINGS
from .utils import parse_date
# Create your views here.

class appointmentsHome(GenericAPIView):
    
    def get(self, request):
        return Response({"Appointments home"})


class SymptomViewSet(ModelViewSet):

    serializer_class = SymptomSerializer
    queryset = Symptom.objects.all()
    permission_classes = (IsAuthenticated, SymptomPermission, )


class AppointmentViewSet(ModelViewSet):

    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = (IsAuthenticated, AppointmentPremission, )
    
    def create(self, request, *args, **kwargs):

        data = request.data
        _date = parse_date(request.data["date"])
        max = APPOINTMENT_SETTINGS["max_daily_limit"]
        current_day_appointments = Appointment.objects.filter(
            date=datetime(_date[0], _date[1], _date[2]))
        print(current_day_appointments)
        # User's current booking
        user = request.user
        student = StudentProfile.objects.get(user=user)
        students_today_appointment = current_day_appointments.filter(student=student)
        if students_today_appointment.count() >= 1:
            return Response(
                {"msg":"The User already has a appointment booked for today"}, status=status.HTTP_403_FORBIDDEN)
        # Check max_daily_limit
        if current_day_appointments.count() >= max:
            return Response({"msg":"Today's Booking is full"}, status=status.HTTP_403_FORBIDDEN)
        

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"data":serializer.data, "msg":"Appointment created."}, status=status.HTTP_201_CREATED)
    
    
    def list(self, request, *args, **kwargs):
        # GET
        _status = request.GET.get("status")
        from_date = request.GET.get("from_date")
        to_date = request.GET.get("to_date")

        if _status:
            self.queryset = self.queryset.filter(status=_status)
        if from_date:
            self.queryset = self.queryset.filter(Q(date__gte=from_date))
        if to_date:
            self.queryset = self.queryset.filter(Q(date__lte=to_date))
        
        serializer = self.get_serializer(self.queryset, many=True)
        return Response({"data":serializer.data, "msg":"List of Appointments"}, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        # PATCH
        appointment = Appointment.objects.get(id=kwargs["pk"])
        _status = request.data["status"]

        if _status:
            if appointment.status != _status:
                appointment.status = _status
                appointment.save()

                all_next_appointments = Appointment.objects.filter(
                    date=appointment.date, status="Pending")
                
                appointment_attended.send(
                    sender=Appointment, 
                    appointment_attended=appointment, 
                    all_next_appointments=all_next_appointments,
                    immediate_next=all_next_appointments.first() 
                    )

                return Response(
                    {"status": f"Appointment {appointment.id} is attended"}, status=status.HTTP_200_OK)
            
            return Response({"status":f"Appointment {appointment.id} already has same status"})

        return Response(
            {"status":f"Appointment {appointment.id} Updated"}, status=status.HTTP_200_OK)
            

class PriscriptionViewSet(ModelViewSet):

    serializer_class = PrescriptionSerializer
    queryset = Prescription.objects.all()
    permission_classes = (IsAuthenticated, PrescriptionPermission, )


