import pytest
from django.core.exceptions import ValidationError
from django.test import TestCase

from custom_user.models import User


pytestmark = pytest.mark.django_db


class TestCustomerModel:
    def test_customer_model(self, customer_factory):
        customer = customer_factory()
        assert customer.__str__() == f'customer {customer.id}'
        assert customer.__repr__() == f'customer {customer.id}'

    def test_customer_profile_model(self, customer_profile_factory):
        customer_profile = customer_profile_factory()
        assert customer_profile.__str__() == f'profile {customer_profile.customer_id}'
        assert customer_profile.__repr__() == f'profile {customer_profile.customer_id}'


class TestCustomerCreation(TestCase):
    @pytest.mark.django_db
    def test_customer_created_ok(self):
        customer = User(
            username='test',
            mobile_number="0545392934",
            password="123@Jnna",
            email="test@test.com",
            is_customer=True,
        )
        customer.save()
        assert customer.mobile_number == "0545392934"
        qs = User.objects.all()
        assert qs.count() == 1

    def test_customer_not_created_customer_superuser_together(self):
        with pytest.raises(ValidationError):
            customer = User(
                username='test',
                mobile_number="0545392934",
                password="123@Jnna",
                email="test@test.com",
                is_customer=True,
                is_superuser=True
            )
            customer.full_clean()
            customer.save()

    def test_customer_not_created_fail_mobile_number_too_long(self):
        with pytest.raises(ValidationError):
            customer = User(
                username='test',
                mobile_number="05453929341",
                email="test@test.com",
                password="123@Jnna",
                is_customer=True,
            )
            customer.full_clean()


class TestCustomersManager(TestCase):
    def setUp(self):
        return NotImplemented

    def test_customer_created_ok(self):
        customer = User.objects.create_user(
            username='test',
            mobile_number="0545392934",
            email="test@test.com",
            is_customer=True,
        )
        customer.full_clean()
        customer.save()
        assert customer.mobile_number == "0545392934"
        qs = User.objects.all()
        assert qs.count() == 1

    def test_customers_object_manager(self):
        return NotImplemented


# TODO
# Complete Customers object testing
