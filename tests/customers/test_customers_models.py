import pytest
from django.test import TestCase
from customers.models import Customers

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

    def test_customer_created_ok(self):
        customer = Customers(
            mobile_number="0545392934",
            email="test@test.com",
        )
        customer.save()
        assert customer.mobile_number == "0545392934"
        qs = Customers.objects.all()
        assert qs.count() == 1


class TestCustomersManager(TestCase):
    def setUp(self):
        return NotImplemented

    def test_customers_object_manager(self):
        return NotImplemented


# TODO
# Complete Customers object testing
