from django.urls import path
from app_items.views import function_based

urlpatterns = [
    path('<int:pk>/', function_based, name='function-based,'),
]