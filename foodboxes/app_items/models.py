from django.db import models

from foodboxes.settings import MEDIA_ITEMS_IMAGE_DIR


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=MEDIA_ITEMS_IMAGE_DIR, default=None, null=True)
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=13, decimal_places=2)
