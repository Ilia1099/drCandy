import uuid

from .models import Order, Cart
from .serializers import OrderSerializer, CartSerializer
from rest_framework import viewsets
from rest_framework.generics import mixins


class OrderViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    lookup_field = 'customer_id'
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CartViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    lookup_field = 'order_id'
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def retrieve(self, request, *args, **kwargs):
        kwargs['order_id'] = uuid.UUID(kwargs.get('order_id'))
        return super().retrieve(request, *args, **kwargs)
