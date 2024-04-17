import uuid

from django.db import models
from customers.models import Customers


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_id = models.ForeignKey(to=Customers, on_delete=models.SET_NULL, null=True, blank=False)
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
    order_id = models.OneToOneField(to="Order", on_delete=models.CASCADE)
    bakery_id = models.ManyToManyField(to="Bakery")
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


class BakeryTypes(models.Model):
    bakery_type = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.bakery_type

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = "bakery_types"
        verbose_name = 'Bakery Type'
        verbose_name_plural = 'Bakery Types'
        db_table_comment = "Table with all bakery types"


class Bakery(models.Model):
    bakery_name = models.CharField(max_length=255)
    bakery_type_id = models.ForeignKey(to="BakeryTypes", on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="bakery_images", null=True, default=None)
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.bakery_name

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = "bakery"
        verbose_name = 'Bakery'
        verbose_name_plural = 'Bakeries'
        db_table_comment = "Table with all bakeries"


class BakeryDescriptions(models.Model):
    bakery_id = models.OneToOneField(to="Bakery", on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=False, unique=True)
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return "description"

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = "bakery_description"
        verbose_name = 'Bakery Description'
        verbose_name_plural = 'Bakery Descriptions'
        db_table_comment = "Table with all bakery descriptions"


class Ingredients(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    bakery_id = models.ManyToManyField(to="Bakery")
    description = models.TextField(null=False, blank=False)
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = 'ingredients'
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
        db_table_comment = "Table with all ingredients"


# TODO
# test all models
