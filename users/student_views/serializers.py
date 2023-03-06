from users.models import StudentProfile
from rest_framework.serializers import ModelSerializer

class ProfileSerializer(ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = '__all__'