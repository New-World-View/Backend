from rest_framework.serializers import ModelSerializer
from .models import Advantages

class AdvantagesSerializer(ModelSerializer):
    class Meta:
        model = Advantages
        fields = ['id', 'icon', 'title', 'suptitle', 'created_at']