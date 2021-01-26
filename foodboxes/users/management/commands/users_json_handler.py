import requests

from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from users.models import User


url = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json'


class Command(BaseCommand):
    help = 'create/update objects for model User'

    def handle(self, *args, **kwargs):
        def get_username_from_email(email):
            username = email.split('@')[0]
            return username

        recipients = requests.get(url)

        try:
            recipients_json = recipients.json()

            for recipient in recipients_json:
                values_for_update = {}

                values_for_update['email'] = recipient['email']
                values_for_update['username'] = get_username_from_email(recipient['email'])
                values_for_update['password'] = make_password(recipient['password'])
                values_for_update['first_name'] = recipient['info']['name']
                values_for_update['last_name'] = recipient['info']['surname']
                values_for_update['middle_name'] = recipient['info']['patronymic']
                values_for_update['phone_number'] = recipient['contacts']['phoneNumber']
                values_for_update['address'] = recipient['city_kladr']

                user, created = User.objects.update_or_create(
                    id=recipient['id'], defaults=values_for_update
                )

        except requests.exceptions.RequestException as er:
            print("Some Ambiguous Exception:", er)
