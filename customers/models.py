import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from customers.managers.customers_manager import CustomerManager


class Customers(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mobile_number = models.CharField(max_length=10, unique=True, help_text="Use valid number format of 10 digits")
    email = models.EmailField(unique=True, help_text="Use valid email format")
    is_active = models.BooleanField(default=True, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    date_updated = models.DateTimeField(auto_now=True, null=False)

    objects = CustomerManager()

    class Meta:
        db_table = 'customers'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        db_table_comment = "Customer base model, created with most necessary data to place an order"
        ordering = ['id']


class CustomerProfile(models.Model):
    customer_id = models.OneToOneField(to="Customers", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False)
    second_name = models.CharField(max_length=50, null=False)
    profile_img = models.ImageField(upload_to='customer_pictures/', null=True, default=None)
    date_of_birth = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    date_updated = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        db_table = 'customer_profile'
        verbose_name = 'Customer Profile'
        verbose_name_plural = 'Customer Profiles'
        db_table_comment = "Customers profile with additional data, created when user completes registration."
        ordering = ['pk']
        unique_together = (('first_name', 'second_name', 'date_of_birth'),)
        index_together = (('first_name', 'second_name'),)

# TODO
# finish logic for custom objects class
# for reference check: BaseUserManager
