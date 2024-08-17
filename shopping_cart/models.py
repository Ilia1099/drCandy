import uuid
from django.db import models
from custom_user.models import User
from gallery.models import Bakery


class Order(models.Model):
    """ A model for order instances each order is associated with a customer """
    order_statuses = [
        ('c', 'Confirmed'), ('d', 'Delivered'), ('p', 'Pending'), ('rcd', 'Received'),
        ('r', 'Rejected'), ('a', 'Archived'), ('s', 'Suspended'), ('b', 'Basket')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    customer_id = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False)
    status = models.CharField(max_length=4, choices=order_statuses, default='b')
    date_of_placement = models.DateTimeField(auto_now_add=True)
    date_of_delivery = models.DateTimeField(null=True, default=None)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"order_{self.id}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ["-date_of_placement"]


class CartItems(models.Model):
    """ A model for cart instances, each cart is associated with an order """
    order_id = models.ForeignKey(to="Order", on_delete=models.CASCADE, name='order')
    bakery_name = models.CharField(max_length=250, blank=False, null=False)
    quantity = models.IntegerField(null=False, default=0)

    def __str__(self):
        return "cart"

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = "order_items"
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
        db_table_comment = "All items within specified order"

