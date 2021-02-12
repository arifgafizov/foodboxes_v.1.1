from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

from reviews.data import status_сhoices
from users.models import User


class Review(models.Model):
    author = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField()
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100, choices=status_сhoices)

    class Meta:
        verbose_name = _('review')
        verbose_name_plural = _('reviews')

    def __str__(self):
        return 'retriew of ' + self.author.last_name
