from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class CustomerManager(BaseUserManager):
    """
    Custom user model manager for Customers model
    """
    use_in_migrations = True

    def _create_user(self, email, password, mobile_number, **extra_fields):

        email = self.normalize_email(email)
        customer = self.model(mobile_number=mobile_number, email=email, **extra_fields)
        customer.password = make_password(password)
        customer.save(using=self._db)
        return customer

    def create_user(self, email, password, mobile_number, **extra_fields):
        return self.create_user(email, password, mobile_number, **extra_fields)