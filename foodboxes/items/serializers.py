from rest_framework.serializers import ModelSerializer

from .models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'image', 'weight', 'price']
        read_only_fields = ['id', 'image']
