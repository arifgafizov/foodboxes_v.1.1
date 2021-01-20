import requests

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(http_method_names=['GET'])
def function_based(request, pk):
    foodboxes = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json')
    if foodboxes:
        foodboxes_json = foodboxes.json()
        response = {}
        for foodbox in foodboxes_json:
            if foodbox['id'] == pk:
                response['id'] = pk
                response['title'] = foodbox['title']
                response['description'] = foodbox['description']
                response['image'] = foodbox['image']
                response['weight'] = foodbox['weight_grams']
                response['price'] = foodbox['price']
        return Response(response)

    elif foodboxes.status_code == 408:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
