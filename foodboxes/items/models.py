from django.db import models
from django.utils.translation import ugettext as _

from django.conf import settings


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=settings.MEDIA_ITEMS_IMAGE_DIR, default=None, null=True)
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=13, decimal_places=2)

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')

    def __str__(self):
        return self.title
