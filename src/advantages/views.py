from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Advantages
from .serializers import AdvantagesSerializer
class CreateAPIViewAdvantages(CreateAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer

class ListAPIViewAdvantages(ListAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer

class RetrieveUpdateDeleteAPIViewAdvantages(RetrieveUpdateDestroyAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer