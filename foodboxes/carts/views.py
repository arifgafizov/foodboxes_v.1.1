from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404

from .models import Cart, CartItem
from .paginations import CartItemLimitOffsetPagination
from .serializers import CartSerializer, CartItemSerializer


class CartList(RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    #permission_classes = [IsAuthenticated]
    #authentication_classes = (TokenAuthentication,)
    lookup_field = 'user_id'

    def get_object(self):
        return self.request.user


class CartItemList(ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    pagination_class = CartItemLimitOffsetPagination


class CartItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
