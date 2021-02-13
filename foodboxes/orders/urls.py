from django.urls import path

from .views import OrderListCreate


urlpatterns = [
    path('', OrderListCreate.as_view(), name='orders_list'),
    #path('<int:pk>/', ItemDetail.as_view(), name='items_detail'),
]