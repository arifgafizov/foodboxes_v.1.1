from django.urls import path

from .views import CartList, CartItemList, CartItemDetail

urlpatterns = [
    path('carts/', CartList.as_view(), name='carts_list'),
    path('carts/items/', CartItemList.as_view(), name='carts_items_list'),
    path('carts/items/<int:pk>/', CartItemDetail.as_view(), name='carts_items_detail'),
]
