from django.db import models
from django.conf import settings

from carts.models import Cart
from orders.data import choices


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_at = models.DateTimeField()
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders', on_delete=models.CASCADE)
    address = models.CharField(max_length=256)
    cart = models.ForeignKey(Cart, related_name='orders', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=choices)
    total_cost = models.DecimalField(max_digits=13, decimal_places=2)
