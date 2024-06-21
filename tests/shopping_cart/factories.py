import factory
from shopping_cart.models import Cart, Order
from tests.custom_user.factories import CustomerFactory
from tests.gallery.factories import BakeryFactory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    customer_id = factory.SubFactory(CustomerFactory)
    status = 'rcd'


class CartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cart

    order_id = factory.SubFactory(OrderFactory)
    bakery_id = factory.RelatedFactory(BakeryFactory)
    quantity = 1
