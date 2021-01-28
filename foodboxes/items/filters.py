from django_filters import rest_framework as filters

from .models import Item


class ItemFilter(filters.FilterSet):
    class Meta:
        model = Item
        fields = {
            'price': ['gt', 'gte', 'lt', 'lte', 'exact'],
            'weight': ['gt', 'gte', 'lt', 'lte', 'exact'],
        }