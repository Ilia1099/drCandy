import uuid
import json
from typing import List

from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from .models import Order, CartItems
from .serializers import OrderSerializer, CartSerializer
from rest_framework import viewsets
from rest_framework.generics import mixins, get_object_or_404


class OrderViewSet(viewsets.ModelViewSet):
    lookup_field = 'order_id'
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self._append_items(serializer.data["id"], request.data.get("items", []))
        headers = self.get_success_headers(serializer.data)
        response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        response.set_cookie(key="order_id", value=serializer.data["id"])
        return response

    def get_queryset(self):
        return Order.objects.filter(customer_id=self.kwargs['user_id'])

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        order = get_object_or_404(queryset, pk=self.kwargs['order_id'])
        serializer = self.get_serializer(order)
        return Response(serializer.data)

    def _append_items(self, order_id: uuid.UUID, order_items: List[dict]):
        with transaction.atomic():
            try:
                for item in order_items:
                    data = {'order_id': order_id}
                    data.update(item)
                    item = CartItems(**data)
                    item.clean_fields()
                    item.save()
            except ValidationError as e:
                transaction.rollback()


class CartViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        order_id = self.kwargs['order_order_id']
        return CartItems.objects.filter(order_id=order_id)
