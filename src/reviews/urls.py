from django.urls import path
from .views import CreateAPIViewReviews, ListAPIViewReviews, RetrieveUpdateDeleteAPIViewReviews

urlpatterns = [
    path('reviews-create/', CreateAPIViewReviews.as_view(), name='reviews-create'),
    path('reviews/', ListAPIViewReviews.as_view(), name='reviews-get'),
    path('reviews/<int:pk>/', RetrieveUpdateDeleteAPIViewReviews.as_view(), name='reviews-detail'),
]