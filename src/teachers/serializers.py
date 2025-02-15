from rest_framework.serializers import ModelSerializer
from .models import Teachers

class TeachersSerializer(ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['id', 'image', 'username', 'profession', 'description', 'created_at']