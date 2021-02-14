from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView


from .models import Item
from .paginations import ItemPageNumberPagination
from .serializers import ItemSerializer
from .filters import ItemFilter


class ItemList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = ItemPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ItemFilter
    filterset_fields = ['price']
    ordering = ['price']

    def get_object(self):
        return self.request.user

    @method_decorator(cache_page(60 * 5))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    #    USER_CACHE_KEY = 'user_cache_{}'
    #    USER_CACHE_TTL = 5 * 60

    #    key = USER_CACHE_KEY.format(request.user)
    #    cache.set(key='key', value=key, timeout=60)
    #    print(key)
    #    cached_response = cache.get(key)
    #    if cached_response:
    #        print('THIS IS CACHE')
    #        return Response(json.loads(cached_response), status=status.HTTP_200_OK)
    #    else:
    #        print('THIS IS DATABASE')
    #        response = super().list(request, *args, **kwargs)
    #        cache.set(key, json.dumps(response.data), USER_CACHE_TTL)
    #        return response

    #@receiver([post_save, post_delete], sender=User)
    #def invalidate_user_cache(sender, self, instance, **kwargs):
    #    cache.delete(self.USER_CACHE_KEY.format(instance.id))


class ItemDetail(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
