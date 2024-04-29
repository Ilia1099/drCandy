import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from customers.managers.customers_manager import CustomerManager


class Customers(AbstractBaseUser):
    """
    Customers model based on AbstractBaseUser model to inherit password management, necessary for placing order
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mobile_number = models.CharField(max_length=10, unique=True, help_text="Use valid number format of 10 digits")
    email = models.EmailField(unique=True, help_text="Use valid email format")
    is_active = models.BooleanField(default=True, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    date_updated = models.DateTimeField(auto_now=True, null=False)

    objects = CustomerManager()

    def __str__(self):
        return f"customer {self.id}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = 'customers'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        db_table_comment = "Customer base model, created with most necessary data to place an order"
        ordering = ['id']


class CustomerProfile(models.Model):
    """ Model which represents extended customer profile if they decide to register """
    customer_id = models.OneToOneField(to="Customers", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    profile_img = models.ImageField(upload_to='customer_pictures/', null=True, default=None)
    date_of_birth = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    date_updated = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return f"profile {self.customer_id}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = 'customer_profile'
        verbose_name = 'Customer Profile'
        verbose_name_plural = 'Customer Profiles'
        db_table_comment = "Customers profile with additional data, created when user completes registration."
        ordering = ['pk']
        unique_together = (('first_name', 'last_name', 'date_of_birth'),)
        indexes = [
            models.Index(fields=['first_name', 'last_name']),
        ]

