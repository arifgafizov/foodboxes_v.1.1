from django.forms import model_to_dict
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from django.utils.dateparse import parse_datetime

from items.models import Item
from orders.models import Order
from carts.models import Cart
from users.models import User
from reviews.models import Review


class ItemListCase(APITestCase):
    def setUp(self):
        self.items = [Item.objects.create(
            title=f'item {b}',
            description=f'text {b}',
            image=None,
            weight=b,
            price=f'{b}.00'
        )
            for b in range(5)]

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('items:items-list')

    def test_items_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['results'], [{'id': i.id,
                                          'title': i.title,
                                          'description': i.description,
                                          'image': None,
                                          'weight': i.weight,
                                          'price': i.price,
                                          }
                                         for i in self.items])


class ItemRetriveCase(APITestCase):
    def setUp(self):
        self.item = Item.objects.create(
            title='test foods',
            description='something',
            image=None,
            weight=100,
            price='100.00'
        )
        self.url = reverse('items:items-detail', kwargs={'pk': self.item.id})

    def test_items_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': self.item.id,
            'title': self.item.title,
            'description': self.item.description,
            'image': None,
            'weight': self.item.weight,
            'price': self.item.price,
        })



class ReviewListCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='lola999',
            email='lola999@bk.ru',
            first_name='Лолита',
            last_name='Малейкина',
            middle_name='Петровна',
            phone_number='8-919-457-36-60',
            address='Санкт-Петербург',
            )

        self.reviews = [Review.objects.create(
            author=self.user,
            status=f'status {b}',
            text=f'text {b}',
            created_at='2020-06-01 00:00:00',
            published_at='2020-06-02 00:00:00'
        )
            for b in range(5)]

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('reviews:reviews-list')

    def test_items_list(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data, [{'id': i.id,
                                'author': {'id': i.author.id,
                                           'username': i.author.username,
                                           'email': i.author.email,
                                            'first_name': i.author.first_name,
                                            'last_name': i.author.last_name,
                                            'middle_name': i.author.middle_name,
                                            'phone_number': i.author.phone_number,
                                            'address': i.author.address,
                                            },
                                'status': i.status,
                                'text': i.text,
                                'created_at':  i.created_at,
                                'published_at': (parse_datetime(i.published_at)).strftime('%Y-%m-%dT%H:%M:%SZ')
                                }
                                for i in self.reviews])

class ReviewCreateTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('reviews:reviews-list')
        cls.user = User.objects.create(
            username='lola999',
            email='lola999@bk.ru',
            first_name='Лолита',
            last_name='Малейкина',
            middle_name='Петровна',
            phone_number='8-919-457-36-60',
            address='Санкт-Петербург',
            )

    def test(self):

        self.client.force_authenticate(self.user)
        data = {
            'author': self.user.id,
            'status': 'status',
            'text': 'text',
            'created_at': '2020-06-01 00:00:00',
            'published_at': '2020-06-02 00:00:00'
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['id'])
        id = response.data['id']
        self.assertTrue(Review.objects.filter(pk=id).exists())
        note = Review.objects.get(pk=id)
        self.assertEqual(response.data, {'id': id, **data, })
        self.assertEqual(model_to_dict(note), {'id': id, **data, })


class OrderListCase(APITestCase):
    def setUp(self):
        self.item = Item.objects.create(
            title='test foods',
            description='something',
            image=None,
            weight=100,
            price='100.00'
        )
        self.user = User.objects.create(
            email='email1',
            username='username1',
            password='pass1',
            first_name='name',
            last_name='surname',
            middle_name='middle',
            phone_number='1230',
            address='city',
            )

        self.cart = Cart.objects.create(
            #items=[self.item],
            user=self.user,
        )
        self.orders = [Order.objects.create(
            cart=f'{b}',
            status=f'status {b}',
            total_cost=f'{b}.00',
            address=f'address {b}',
            delivery_at=f'2021-02-0{b}',
            created_at=f'2021-02-0{b}',
        )
            for b in range(5)]

        for order in self.orders:
            cart = self.cart.set([self.item])
            order.cart.add(cart)



    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('orders:orders-list')

    def test_orders_list(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['results'], [{'id': i.id,
                                          'cart': i.cart,
                                          'status': i.status,
                                          'total_cost': i.total_cost,
                                          'address': i.address,
                                          'delivery_at': i.delivery_at,
                                          'created_at': i.created_at
                                          }
                                         for i in self.orders])
