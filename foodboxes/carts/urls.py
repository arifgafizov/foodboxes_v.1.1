from django.urls import path

from .views import CartList


urlpatterns = [
    path('carts/', CartList.as_view(), name='carts_list'),
]
