from django.shortcuts import render
from .models import Reviews
from .serializers import ReviewsSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from src.permissions import IsAuthenticatedForWrite 
# Create your views here.

class ReviewsPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100

class CreateAPIViewReviews(generics.CreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [AllowAny]

class ListAPIViewReviews(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    pagination_class = ReviewsPagination
    permission_classes = [AllowAny]

class RetrieveUpdateDeleteAPIViewReviews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthenticatedForWrite] 