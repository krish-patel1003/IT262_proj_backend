from users.models import StudentProfile
from rest_framework.viewsets import ModelViewSet
from .serializers import ProfileSerializer
from .permissions import UpdateOwnProfile
from django_filters.rest_framework import DjangoFilterBackend
from users.models import User
from rest_framework.response import Response
from rest_framework import status

class ProfileViewSet(ModelViewSet):
    
    serializer_class = ProfileSerializer
    queryset = StudentProfile.objects.all()
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('rollno',)

    def retrieve(self, request, *args, **kwargs):
        _id = kwargs["pk"]
        try:
            student = self.queryset.get(id=_id)
        except StudentProfile.DoesNotExist:
            return Response({"error": "No student with that id exists"}, status=status.HTTP_204_NO_CONTENT)
        user = User.objects.get(id=student.user.id)
        data = self.serializer_class(student).data
        data["name"] = user.get_full_name()
        data["email"] = user.email
        data["phone"] = user.phone

        return Response({"data": data, "msg": "Student user fetched"}, status=status.HTTP_200_OK)

