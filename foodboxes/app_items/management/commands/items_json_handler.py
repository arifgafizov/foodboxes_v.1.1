import requests

from django.core.management.base import BaseCommand

from app_items.models import Item


class Command(BaseCommand):
    help = 'create objects for model Item'

    def handle(self, *args, **kwargs):
        foodboxes = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json')

        if foodboxes:
            foodboxes_json = foodboxes.json()

            for foodbox in foodboxes_json:
                item = Item.objects.filter(id=foodbox['id']).first()
                if not item:
                    new_item = Item.objects.create(
                        title=foodbox['name'],
                        description=foodbox['description'],
                        image=foodbox['image'],
                        weight=foodbox['weight_grams'],
                        price=foodbox['price']
                    )
                    self.stdout.write(f"The item {new_item.title} is created")
                else:
                    item.save()
                    self.stdout.write(f"The item {item.title} updated")

        elif foodboxes.status_code == 408:
            return self.stdout.write("408 REQUEST TIMEOUT")

        else:
            return self.stdout.write("404 NOT FOUND")
