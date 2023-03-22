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
from datetime import datetime, date
# Create your views here.

class NoticeViewSet(ModelViewSet):

    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()
    permission_classes = [IsAuthenticated, NoticePermission]

    def create(self, request, *args, **kwargs):
        print(request.data)
        data = request.data
        on_leave_from = date(*parse_date(data["on_leave_from"]))
        on_leave_till = date(*parse_date(data["on_leave_till"]))
        today = datetime.today().date()

        print("values - >", on_leave_from, on_leave_till, today)
        if data["tag"] == "Leave":
            if on_leave_from == today:
                print("Emergency Leave")

                if on_leave_till and on_leave_till > today:
                    print("emergency leave of multiple days")
            
                if on_leave_till and on_leave_till == today:
                    print("emergency leave of one day")
            
            else:
                print("Leave declared in advanced")
        
        return super().create(self, request, *args, **kwargs)


    

