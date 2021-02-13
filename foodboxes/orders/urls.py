from django.urls import path

from .views import OrderList


urlpatterns = [
    path('', OrderList.as_view(), name='orders_list'),
    #path('<int:pk>/', ItemDetail.as_view(), name='items_detail'),
]