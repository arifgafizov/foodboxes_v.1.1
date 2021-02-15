from rest_framework.serializers import ModelSerializer

from .models import Order
from carts.serializers import CartSerializer
from users.serializers import UserSerializer


class OrderListSerializer(ModelSerializer):
    cart = CartSerializer()

    class Meta:
        model = Order
        fields = ['id', 'cart', 'status', 'total_cost', 'address', 'delivery_at', 'created_at']


class OrderDetailSerializer(ModelSerializer):
    cart = CartSerializer()
    recipient = UserSerializer()

    class Meta:
        model = Order
        fields = ['id', 'cart', 'status', 'recipient', 'total_cost', 'address', 'delivery_at', 'created_at']


class OrderUpdateSerializer(ModelSerializer):
    cart = CartSerializer()

    class Meta:
        model = Order
        fields = ['id', 'cart', 'status', 'address', 'delivery_at']