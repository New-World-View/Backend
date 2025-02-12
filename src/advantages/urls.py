from django.urls import path
from .views import CreateAPIViewAdvantages, ListAPIViewAdvantages

urlpatterns = [
    path('advantages-create/', CreateAPIViewAdvantages.as_view(), name='advantages-create'),
    path('advantages/', ListAPIViewAdvantages.as_view(), name='advantages-get'),
]