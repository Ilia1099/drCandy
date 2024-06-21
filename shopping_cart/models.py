import uuid
from django.db import models
from custom_user.models import User
from gallery.models import Bakery


class Order(models.Model):
    """ A model for order instances each order is associated with a customer """
    order_statuses = [
        ('c', 'Confirmed'), ('d', 'Delivered'), ('p', 'Pending'), ('rcd', 'Received'),
        ('r', 'Rejected'), ('a', 'Archived'), ('s', 'Suspended')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_id = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False)
    status = models.CharField(max_length=4, choices=order_statuses, default='rcd')
    date_of_placement = models.DateTimeField(auto_now_add=True)
    date_of_delivery = models.DateTimeField(null=True, default=None)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "order"

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ["-date_of_placement"]


class Cart(models.Model):
    """ A model for cart instances, each cart is associated with an order """
    order_id = models.OneToOneField(to="Order", on_delete=models.CASCADE)
    bakery_id = models.ManyToManyField(to=Bakery)
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

