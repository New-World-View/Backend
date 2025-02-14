from rest_framework.serializers import ModelSerializer
from .models import Cources

class CourcesSerializer(ModelSerializer):
    class Meta:
        model = Cources
        fields = ['id', 'image', 'name_coursec', 'price', 'title', 'suptitle', 'info_course', 'teachers', 'created_at']