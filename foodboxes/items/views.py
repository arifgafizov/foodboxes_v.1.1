from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Item


@api_view(http_method_names=['GET'])
def function_based(request, pk):
    item = get_object_or_404(Item, pk=pk)
    response = {
        "id": item.id,
        "title": item.title,
        "description": item.description,
        "image": item.image.url,
        "weight": item.weight,
        "price": item.price
    }
    return Response(response)
