from django.urls import path

from .views import ReviewListCreate


urlpatterns = [
    path('', ReviewListCreate.as_view(), name='reviews-list'),
]