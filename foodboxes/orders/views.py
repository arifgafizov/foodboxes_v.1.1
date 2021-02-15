from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Order
from .serializers import OrderListSerializer, OrderDetailSerializer, OrderUpdateSerializer


class OrderListCreate(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Order.objects.filter(recipient=self.request.user)


class OrderItemDetail(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)


    def get_queryset(self):
        return Order.objects.filter(recipient=self.request.user)

    def update(self, request, *args, **kwargs):
        order = get_object_or_404(self.queryset.filter(recipient=self.request.user))
        serializer = OrderUpdateSerializer(order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data.get('status') == 'created':
            serializer.save()
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        return Response('Order status is not created', status=status.HTTP_400_BAD_REQUEST)
