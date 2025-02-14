from rest_framework import generics
from .models import Cources
from .serializers import CourcesSerializer

class CreateAPIViewCources(generics.CreateAPIView):
    queryset = Cources.objects.all()
    serializer_class = CourcesSerializer

class ListAPIViewCources(generics.ListAPIView):
    queryset = Cources.objects.all()
    serializer_class = CourcesSerializer