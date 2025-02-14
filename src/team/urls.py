from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import CreateApiViewTeam, ListAPIViewTeam, RetrieveUpdateDeleteAPIViewTeam

schema_view = get_schema_view(
    openapi.Info(
        title="Team API Documentation",
        default_version='v1',
        description="API documentation for Team CRUD operations",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('team-create/', CreateApiViewTeam.as_view(), name='team-create'),
    path('team/', ListAPIViewTeam.as_view(), name='team-get'),
    path('team/<int:pk>/', RetrieveUpdateDeleteAPIViewTeam.as_view(), name='team-detail'),
]
