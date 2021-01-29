from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Cart, CartItem
from .paginations import CartItemLimitOffsetPagination
from .serializers import CartSerializer, CartItemSerializer


class CartList(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemList(ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    pagination_class = CartItemLimitOffsetPagination

class CartItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
