from django.db import models

from app_reviews.data import statusChoices
from app_users.models import User


class Review(models.Model):
    author = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()
    published_at = models.DateTimeField()
    status = models.CharField(max_length=100, choices=statusChoices)
