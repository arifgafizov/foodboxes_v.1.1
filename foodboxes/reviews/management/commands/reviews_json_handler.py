import requests

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand

from reviews.models import Review


class Command(BaseCommand):
    help = 'create/update objects for model Review'

    def handle(self, *args, **kwargs):
        url = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/reviews.json'
        reviews = requests.get(url)
        try:
            reviews_json = reviews.json()

            for review in reviews_json:
                values_for_update = {}

                values_for_update['text'] = review['content']
                values_for_update['created_at'] = review['created_at']
                values_for_update['published_at'] = review['published_at']
                values_for_update['status'] = review['status']
                values_for_update['author_id'] = review['author']

                try:
                    review_obj, created = Review.objects.update_or_create(
                        id=review['id'], defaults=values_for_update
                    )
                except ValidationError:
                    print('Value has an invalid format. It must be in YYYY-MM-DD HH:MM')

        except requests.exceptions.RequestException as er:
            print("Some Ambiguous Exception:", er)
