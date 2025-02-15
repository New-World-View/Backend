from rest_framework import generics
from .models import Cources
from .serializers import CourcesSerializer, CourcesGetAllSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from src.permissions import IsAuthenticatedForWrite 

class CreateAPIViewCources(generics.CreateAPIView):
    queryset = Cources.objects.all()
    serializer_class = CourcesSerializer
    permission_classes = [IsAuthenticated]  

class ListAPIViewCources(generics.ListAPIView):
    queryset = Cources.objects.all()
    serializer_class = CourcesGetAllSerializer
    permission_classes = [AllowAny]  

class RetrieveUpdateDeleteAPIViewCources(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourcesSerializer
    permission_classes = [IsAuthenticatedForWrite] 

    def get_queryset(self):
        queryset = Cources.objects.all()
        name_coursec = self.request.query_params.get("name_coursec")

        if name_coursec:
            queryset = queryset.filter(name_coursec=name_coursec)

        return queryset