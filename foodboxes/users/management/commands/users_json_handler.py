import requests

from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'create objects for model User'

    def handle(self, *args, **kwargs):
        recipients = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json')
        if recipients:
            recipients_json = recipients.json()

            for recipient in recipients_json:
                values_for_update = {}

                values_for_update['email'] = recipient['email']
                values_for_update['username'] = recipient['email'].split('@')[0]
                values_for_update['password'] = recipient['password']
                values_for_update['first_name'] = recipient['info']['name']
                values_for_update['last_name'] = recipient['info']['surname']
                values_for_update['middle_name'] = recipient['info']['patronymic']
                values_for_update['phone_number'] = recipient['contacts']['phoneNumber']
                values_for_update['address'] = recipient['city_kladr']

                user, created = User.objects.update_or_create(
                    id=recipient['id'], defaults=values_for_update
                )

        elif recipients.status_code == 408:
            return self.stdout.write("408 REQUEST TIMEOUT")

        else:
            return self.stdout.write("404 NOT FOUND")
