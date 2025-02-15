from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Advantages
from .serializers import AdvantagesSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from src.permissions import IsAuthenticatedForWrite 
class CreateAPIViewAdvantages(CreateAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer
    permission_classes = [IsAuthenticated]  

class ListAPIViewAdvantages(ListAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer
    permission_classes = [AllowAny]  

class RetrieveUpdateDeleteAPIViewAdvantages(RetrieveUpdateDestroyAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer
    permission_classes = [IsAuthenticatedForWrite] 