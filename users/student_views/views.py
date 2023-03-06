from users.models import StudentProfile
from rest_framework.viewsets import ModelViewSet
from .serializers import ProfileSerializer
from .permissions import UpdateOwnProfile
from django_filters.rest_framework import DjangoFilterBackend

class ProfileViewSet(ModelViewSet):
    
    serializer_class = ProfileSerializer
    queryset = StudentProfile.objects.all()
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('rollno',)
