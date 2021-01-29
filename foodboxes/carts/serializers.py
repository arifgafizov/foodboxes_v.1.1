from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Cart


class CartSerializer(ModelSerializer):
    total_cost = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_cost']
        read_only_fields = ['id', 'items']
