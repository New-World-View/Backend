from django.urls import path
from .views import CreateAPIViewCources, ListAPIViewCources

urlpatterns = [
    path('cources-create/', CreateAPIViewCources.as_view(), name='cources-create'),
    path('cources/', ListAPIViewCources.as_view(), name='cources-get'),
]