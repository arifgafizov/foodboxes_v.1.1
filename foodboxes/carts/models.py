from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

from items.models import Item


class Cart(models.Model):
    items = models.ManyToManyField(to=Item, through="CartItem")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='carts', on_delete=models.CASCADE)

    @property
    def total_cost(self):
        return self.cart_items.price.data * self.cart_items.quantity.data


class CartItem(models.Model):
    item = models.ForeignKey(Item, related_name='cart_items', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=13, decimal_places=2)

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')

    def __str__(self):
        return 'cart of ' + self.user.last_name

    @property
    def total_price(self):
        return self.price * self.quantity
