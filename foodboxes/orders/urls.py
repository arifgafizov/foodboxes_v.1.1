from django.urls import path

from .views import OrderListCreate, OrderItemDetail


urlpatterns = [
    path('', OrderListCreate.as_view(), name='orders_list'),
    path('<int:pk>/', OrderItemDetail.as_view(), name='orders_detail'),
]