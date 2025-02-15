from rest_framework import serializers
from .models import Cources
from teachers.models import Teachers
from teachers.serializers import TeachersSerializer

class CourcesSerializer(serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = Cources
        fields = "__all__"

    def get_teachers(self, obj):
        teachers = Teachers.objects.filter(profession=obj.name_coursec)
        return TeachersSerializer(teachers, many=True).data

class CourcesGetAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cources
        fields = ['id', 'image', 'title', 'price', 'created_at']

    