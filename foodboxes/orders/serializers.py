from rest_framework.serializers import ModelSerializer

from .models import Order
from carts.serializers import CartSerializer
from users.serializers import UserSerializer


class OrderSerializer(ModelSerializer):
    cart = CartSerializer()

    class Meta:
        model = Order
        fields = ['id', 'cart', 'status', 'total_cost', 'address', 'delivery_at', 'created_at']
