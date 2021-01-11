import requests

from django.core.management.base import BaseCommand
from rest_framework import status
from rest_framework.response import Response

from app_items.models import Item


class Command(BaseCommand):
    help = 'create objects for model Item'

    def handle(self, *args, **kwargs):
        foodboxes = requests.get('https://stepik.org/media/attachments/course/73594/foodboxes.json')

        if foodboxes:
            foodboxes_json = foodboxes.json()

            for foodbox in foodboxes_json:
                item = Item.objects.filter(id=foodbox['inner_id']).first()
                if not item:
                    new_item = Item.objects.create(
                        title=foodbox['name'],
                        description=foodbox['about'],
                        image=foodbox['images']['full'],
                        weight=foodbox['weight_grams'],
                        price=foodbox['price']
                    )
                    self.stdout.write(f"The item {foodbox['name']} is created")
                else:
                    item.save()
                    self.stdout.write(f"The item {foodbox['name']} updated")


        elif foodboxes.status_code == 408:
            return Response(status=status.HTTP_408_REQUEST_TIMEOUT)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
