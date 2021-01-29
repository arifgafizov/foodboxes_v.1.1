from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Cart, CartItem


class CartSerializer(ModelSerializer):
    total_cost = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_cost']
        read_only_fields = ['id', 'items']

class CartItemSerializer(ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = CartItem
        fields = ['id', 'item', 'quantity', 'price', 'total_price']
        read_only_fields = ['id', 'price']
