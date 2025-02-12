from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Advantages
from .serializers import AdvantagesSerializer
# Create your views here.

class CreateAPIViewAdvantages(CreateAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer

class ListAPIViewAdvantages(ListAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer