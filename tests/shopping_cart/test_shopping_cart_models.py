import pytest

pytestmark = pytest.mark.django_db


class TestShoppingCartModels:
    def test_order_model(self, order_factory):
        order = order_factory()
        assert order.__str__() == "order"
        assert order.__repr__() == "order"

    def test_shopping_cart_model(self, cart_factory):
        shopping_cart = cart_factory()
        assert shopping_cart.__str__() == "cart"
        assert shopping_cart.__repr__() == "cart"
