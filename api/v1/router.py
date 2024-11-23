from rest_framework_nested import routers
from gallery.views import BakeryViewSet, IngredientViewSet, BakeryTypeViewSet
from shopping_cart.views import OrderViewSet, CartViewSet
from custom_user.views import UsersViewSet, CustomerProfileViewSet
from django.urls import path, include

base_router = routers.DefaultRouter()
base_router.register(r'account', UsersViewSet, basename='account')
base_router.register(r'bakeries', BakeryViewSet)
base_router.register(r'ingredients', IngredientViewSet)
base_router.register(r'bakery_types', BakeryTypeViewSet)

account_router = routers.NestedSimpleRouter(base_router, r'account', lookup='user')
account_router.register('orders', OrderViewSet, basename='orders')
account_router.register('profile', CustomerProfileViewSet, basename='profile')

orders_router = routers.NestedSimpleRouter(account_router, r'orders', lookup='order')
orders_router.register(r'items', CartViewSet, basename='items')


urlpatterns = [
    path('', include(base_router.urls)),
    path('', include(account_router.urls)),
    path('', include(orders_router.urls)),
]

# Todo
# rework userviewst - change of password should not be mandatory