from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Notice
from .serializers import NoticeSerializer
from .permissions import NoticePermission
# Create your views here.

class NoticeViewSet(ModelViewSet):

    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()
    permission_classes = [IsAuthenticated, NoticePermission]

    

