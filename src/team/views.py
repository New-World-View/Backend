from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Team
from .serializers import TeamSerializer

# Кастомная пагинация
class TeamPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100

class CreateApiViewTeam(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ListAPIViewTeam(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = TeamPagination  
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['profession']  
