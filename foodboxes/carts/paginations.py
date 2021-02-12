from rest_framework.pagination import LimitOffsetPagination


class CartItemLimitOffsetPagination(LimitOffsetPagination):
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 6
