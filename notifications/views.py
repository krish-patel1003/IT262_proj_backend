from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Notice
from .serializers import NoticeSerializer
from .permissions import NoticePermission
from .signals import emergency_leave
from appointments.utils import parse_date
from datetime import datetime, date, timedelta
from appointments.models import Appointment
# Create your views here.

class NoticeViewSet(ModelViewSet):

    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()
    permission_classes = [IsAuthenticated, NoticePermission]

    def reschedule(self, on_leave_from, on_leave_till):
        print("rescheduling")
        appointments = Appointment.objects.filter(date=on_leave_from)
        for appointment in appointments:
            print("appointments: ", appointment.date)
            appointment.save(date=on_leave_till+timedelta(days=1))
            print("rescheduled apmt: ", appointment.date)
        

    def create(self, request, *args, **kwargs):
        # print(request.data)
        data = request.data
        on_leave_from = date(*parse_date(data["on_leave_from"]))
        on_leave_till = date(*parse_date(data["on_leave_till"]))
        today = datetime.today().date()

        # print("values - >", on_leave_from, on_leave_till, today)
        if data["tag"] == "Leave":
            if on_leave_from == today:
                print("Emergency Leave")

                if on_leave_till and on_leave_till > today:
                    print("emergency leave of multiple days")
                    self.reschedule(today, on_leave_till)
            
                if on_leave_till and on_leave_till == today:
                    print("emergency leave of one day")
                    self.reschedule(today, on_leave_till)
            else:
                print("Leave declared in advanced")
                self.reschedule(on_leave_from, on_leave_till)
        
        return super().create(request, *args, **kwargs)




