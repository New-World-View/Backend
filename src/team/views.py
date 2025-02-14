from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Team
from .serializers import TeamSerializer

class TeamPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100

class CreateApiViewTeam(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @swagger_auto_schema(
        operation_description="Create a new team entry.",
        request_body=TeamSerializer,
        responses={201: TeamSerializer},
    )
    def post(self, request, *args, **kwargs):
        """
        Handles creating a new team object.
        """
        return super().post(request, *args, **kwargs)

class ListAPIViewTeam(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = TeamPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['profession']

    @swagger_auto_schema(
        operation_description="Retrieve a list of teams with optional filtering by profession.",
        responses={200: TeamSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        """
        Handles retrieving a paginated list of teams.
        """
        return super().get(request, *args, **kwargs)

class RetrieveUpdateDeleteAPIViewTeam(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @swagger_auto_schema(
        operation_description="Retrieve details of a team by ID.",
        responses={200: TeamSerializer, 404: "Team not found"},
    )
    def get(self, request, *args, **kwargs):
        """
        Handles retrieving a single team by its ID.
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update details of a team by ID.",
        request_body=TeamSerializer,
        responses={200: TeamSerializer},
    )
    def put(self, request, *args, **kwargs):
        """
        Handles updating a team by its ID.
        """
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a team by ID.",
        responses={204: "No Content", 404: "Team not found"},
    )
    def delete(self, request, *args, **kwargs):
        """
        Handles deleting a team by its ID.
        """
        return super().delete(request, *args, **kwargs)
