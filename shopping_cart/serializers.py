from rest_framework import serializers
from .models import Order, CartItems


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer_id', 'status', 'date_of_delivery', 'date_of_placement', 'date_updated']
        read_only_fields = ['id', 'status', 'date_of_delivery', 'date_of_placement', 'date_updated']
        required_fields = ['customer_id']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ['id', 'order_id', 'bakery_name', 'quantity']
        read_only_fields = ['id',]
        required_fields = ['order_id', 'bakery_name', 'quantity']
