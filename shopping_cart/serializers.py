from rest_framework import serializers
from .models import Order, Cart


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer_id', 'status', 'date_of_delivery', 'date_of_placement', 'date_updated']
        read_only_fields = ['id', 'status', 'date_of_delivery', 'date_of_placement', 'date_updated']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'order_id', 'bakery_id', 'quantity']
        read_only_fields = ['id', 'order_id', 'bakery_id']
