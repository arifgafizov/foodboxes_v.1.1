from django.db import models
from django.utils.translation import ugettext as _

from items.models import Item
from users.models import User


class Cart(models.Model):
    items = models.ManyToManyField(to=Item, through="CartItem", related_name='carts')
    user = models.ForeignKey(User, related_name='carts', on_delete=models.CASCADE)

    def total_cost(self):
        return 'stuff'

class CartItem(models.Model):
    item = models.ForeignKey(Item, related_name='cart_items', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=13, decimal_places=2)

    def total_price(self):
        return 'stuff'

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')

    def __str__(self):
        return 'cart of ' + self.user.last_name
