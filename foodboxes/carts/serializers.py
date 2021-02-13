from rest_framework.serializers import ModelSerializer

from .models import Cart, CartItem
from items.serializers import ItemSerializer


class CartSerializer(ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['user', 'id', 'items', 'total_cost']


class CartItemSerializer(ModelSerializer):
    item = ItemSerializer(many=True)
    cart = CartSerializer(many=True)

    class Meta:
        model = CartItem
        fields = ['id', 'item', 'quantity', 'price', 'cart', 'total_price']
        read_only_fields = ['id', 'price']
