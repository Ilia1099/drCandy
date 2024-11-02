from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from custom_user.model_managers.customers_manager import UserManager
from django.conf import settings


def mobile_number_validator(value):
    if len(value) != 10:
        raise ValidationError("Mobile Number must be 10 digits long")


class User(AbstractUser):
    """
    Custom User model based on AbstractBaseUser model to inherit password management, necessary for placing order
    has additional type of user to implement specific authorization
    """
    is_customer = models.BooleanField(default=False)
    mobile_number = models.CharField(
        validators=[mobile_number_validator],
        max_length=10, blank=True, null=True,
        help_text="Use valid number 10 digits"
    )

    objects = UserManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.is_customer and self.is_superuser:
            raise ValidationError("You can't be a customer and a superuser")

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return self.__str__()


class CustomerProfile(models.Model):
    """ Model which represents extended customer profile if they decide to register """
    customer_id = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='customer_pictures/', null=True, default=None)
    date_of_birth = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    date_updated = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return f"profile of user: {self.customer_id}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = 'customer_profile'
        verbose_name = 'Customer Profile'
        verbose_name_plural = 'Customer Profiles'
        db_table_comment = "Customers profile with additional data, created when user completes registration."
        ordering = ['pk']
        unique_together = (('customer_id', 'date_of_birth'),)
