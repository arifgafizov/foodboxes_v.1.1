from rest_framework.serializers import ModelSerializer

from .models import Cart, CartItem
from items.serializers import ItemSerializer


class CartSerializer(ModelSerializer):

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_cost']
        read_only_fields = ['id', 'items']

class CartItemSerializer(ModelSerializer):
    item = ItemSerializer(many=True)
    car = CartSerializer(many=True)

    class Meta:
        model = CartItem
        fields = ['id', 'item', 'quantity', 'price', 'car', 'total_price']
        read_only_fields = ['id', 'price']
