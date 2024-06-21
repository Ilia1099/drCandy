from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import make_password


class CustomUserManager(UserManager):
    """
    Custom user model manager for Customers model
    """
    use_in_migrations = True

    def _create_customer(self, email, password, **extra_fields):
        staff = self.create_user(email, password, **extra_fields)
        staff.is_customer = True
        staff.save()

    def create_customer(self, email, password, **extra_fields):
        return self._create_customer(email, password, **extra_fields)
    #
    # def _create_user(self, email, password, mobile_number, **extra_fields):
    #
    #     email = self.normalize_email(email)
    #     customer = self.model(mobile_number=mobile_number, email=email, **extra_fields)
    #     customer.password = make_password(password)
    #     customer.save(using=self._db)
    #     return customer
    #
    # def create_user(self, email, password, mobile_number, **extra_fields):
    #     return self._create_user(email, password, mobile_number, **extra_fields)
