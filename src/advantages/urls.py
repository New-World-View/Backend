from django.urls import path
from .views import CreateAPIViewAdvantages, ListAPIViewAdvantages, RetrieveUpdateDeleteAPIViewAdvantages

urlpatterns = [
    path('advantages-create/', CreateAPIViewAdvantages.as_view(), name='advantages-create'),
    path('advantages/', ListAPIViewAdvantages.as_view(), name='advantages-get'),
    path('advantages/<int:pk>/', RetrieveUpdateDeleteAPIViewAdvantages.as_view(), name='advantages-detail'),

]