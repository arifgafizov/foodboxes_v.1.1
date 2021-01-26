from django.urls import path
from items.views import function_based

urlpatterns = [
    path('<int:pk>/', function_based, name='function-based,'),
]
