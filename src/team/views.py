from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Team
from .serializers import TeamSerializer
from src.permissions import IsAuthenticatedForWrite 

class TeamPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100

class CreateApiViewTeam(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]  

class ListAPIViewTeam(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = TeamPagination  
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['profession']  
    permission_classes = [AllowAny]  

class RetrieveUpdateDeleteAPIViewTeam(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticatedForWrite] 
