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
from rest_framework.generics import mixins


class OrderViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    lookup_field = 'id'
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
