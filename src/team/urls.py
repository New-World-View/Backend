from django.urls import path
from .views import CreateApiViewTeam, ListAPIViewTeam, RetrieveUpdateDeleteAPIViewTeam

urlpatterns = [
    path('team-create/', CreateApiViewTeam.as_view(), name='team-create'),
    path('team/', ListAPIViewTeam.as_view(), name='team-get'),
    path('team/<int:pk>/', RetrieveUpdateDeleteAPIViewTeam.as_view(), name='team-detail'),
]