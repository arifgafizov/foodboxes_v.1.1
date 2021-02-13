from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.conf import settings

from reviews.data import status_сhoices


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100, choices=status_сhoices)

    class Meta:
        verbose_name = _('review')
        verbose_name_plural = _('reviews')

    def __str__(self):
        return 'review of ' + self.author.last_name
