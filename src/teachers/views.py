from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Teachers
from .serializers import TeachersSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from src.permissions import IsAuthenticatedForWrite 

class TeachersPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100

class CreateApiViewTeachers(CreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    permission_classes = [IsAuthenticated]  

class ListAPIViewTeachers(ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    pagination_class = TeachersPagination  
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['profession']  
    permission_classes = [AllowAny]  

class RetrieveUpdateDeleteAPIViewTeachers(RetrieveUpdateDestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    permission_classes = [IsAuthenticatedForWrite] 