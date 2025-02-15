from django.urls import path
from .views import CreateApiViewTeachers, ListAPIViewTeachers, RetrieveUpdateDeleteAPIViewTeachers

urlpatterns = [
    path('teachers-create/', CreateApiViewTeachers.as_view(), name='teachers-create'),
    path('teachers/', ListAPIViewTeachers.as_view(), name='teachers-get'),
    path('teachers/<int:pk>/', RetrieveUpdateDeleteAPIViewTeachers.as_view(), name='teachers-detail'),
]