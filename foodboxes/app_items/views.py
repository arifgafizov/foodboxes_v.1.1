from rest_framework.viewsets import ViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from app_items.models import ItemSerializer, Item


class ItemViewset(ViewSet):
    def list(self, request):
        queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Item.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
