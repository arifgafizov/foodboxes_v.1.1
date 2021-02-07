from django.urls import path

from .views import ItemList, ItemDetail


urlpatterns = [
    path('', ItemList.as_view(), name='items_list'),
    path('<int:pk>/', ItemDetail.as_view(), name='items_detail'),
]
