from rest_framework.serializers import ModelSerializer
from .models import Team

class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'image', 'username', 'profession', 'description', 'created_at']