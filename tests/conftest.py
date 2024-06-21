from pytest_factoryboy import register
from .custom_user.factories import CustomerFactory, CustomerProfileFactory
from .gallery.factories import BakeryFactory, BakeryTypeFactory, IngredientsFactory, DescriptionFactory
from .shopping_cart.factories import OrderFactory, CartFactory

register(CustomerFactory)
register(CustomerProfileFactory)
register(BakeryFactory)
register(BakeryTypeFactory)
register(IngredientsFactory)
register(DescriptionFactory)
register(OrderFactory)
register(CartFactory)
