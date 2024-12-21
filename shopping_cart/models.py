import uuid
from django.db import models
from custom_user.models import User


class Order(models.Model):
    """ A model for order instances each order is associated with a customer """
    order_statuses = [
        ('c', 'Confirmed'), ('d', 'Delivered'), ('p', 'Pending'), ('rcd', 'Received'),
        ('r', 'Rejected'), ('a', 'Archived'), ('s', 'Suspended'), ('b', 'Basket'), ('prcg', 'Processing'),
        ('shpd', 'Shipping')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    customer_id = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False)
    status = models.CharField(max_length=4, choices=order_statuses, default='b')
    date_of_placement = models.DateTimeField(auto_now_add=True)
    date_of_delivery = models.DateTimeField(null=True, default=None)
    date_updated = models.DateTimeField(auto_now=True)
    # TODO
    # write custom validation on fields, checking order_status, if status == 'b' then could be saved
    # also status field must check permission cos only authorized users should be able to change it (admin)

    def __str__(self):
        return f"order_{self.id}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ["-date_of_placement"]


class CartItem(models.Model):
    """ A model for cart instances, each cart is associated with an order """
    order_id = models.ForeignKey(to="Order", related_name='cart_item', on_delete=models.CASCADE, name='order')
    bakery_name = models.CharField(max_length=250, blank=False, null=False)
    quantity = models.IntegerField(null=False, default=0)

    def __str__(self):
        return "cart"

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = "cart_item"
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'
        db_table_comment = "All items within specified order"

