import requests

from django.core.management.base import BaseCommand

from app_items.models import Item
from foodboxes.settings import MEDIA_ITEMS_IMAGE_DIR


class Command(BaseCommand):
    help = 'create objects for model Item'

    def handle(self, *args, **kwargs):
        def parser_images(responses):
            responses_json = responses.json()

            for response in responses_json:
                url_img = response['image']
                name_img = url_img.split('/')[-1]
                print(name_img, 'successfully downloaded to ./media/items_images')

                p = requests.get(url_img)
                out = open('./media/' + MEDIA_ITEMS_IMAGE_DIR + '/' + name_img, "wb")
                out.write(p.content)
                out.close()

        foodboxes = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json')

        if foodboxes:
            parser_images(foodboxes)
            foodboxes_json = foodboxes.json()

            for foodbox in foodboxes_json:
                values_for_update = {}

                values_for_update['title'] = foodbox['title']
                values_for_update['description'] = foodbox['description']
                values_for_update['image'] = MEDIA_ITEMS_IMAGE_DIR + '/' + foodbox['image'].split('/')[-1]
                values_for_update['weight'] = foodbox['weight_grams']
                values_for_update['price'] = foodbox['price']

                user, created = Item.objects.update_or_create(
                    id=foodbox['id'], defaults=values_for_update
                )

        elif foodboxes.status_code == 408:
            return self.stdout.write("408 REQUEST TIMEOUT")

        else:
            return self.stdout.write("404 NOT FOUND")
