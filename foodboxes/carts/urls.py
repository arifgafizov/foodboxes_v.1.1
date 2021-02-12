from django.urls import path

from .views import CartItemList, CartItemDetail, CartList


urlpatterns = [
    path('', CartList.as_view(), name='carts_list'),
    path('items/', CartItemList.as_view(), name='carts_items_list'),
    path('items/<int:pk>/', CartItemDetail.as_view(), name='carts_items_detail'),
]
