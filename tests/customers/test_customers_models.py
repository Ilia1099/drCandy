import pytest

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
