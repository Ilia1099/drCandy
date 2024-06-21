from django.test import TestCase
import pytest_django
from custom_user.models import User
import pytest


class TestUserCreation(TestCase):
    # @pytest.mark.django_db
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='test',
            mobile_number="0545392934",
            password="123@Jnna",
            email="test@test.com",
            is_customer=True,
        )

    def test_customer_create(self):
        assert self.user.username == "test"

# Create your tests here.
