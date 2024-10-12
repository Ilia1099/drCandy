from rest_framework_nested import routers
from gallery.views import BakeryViewSet, IngredientViewSet, BakeryTypeViewSet
from shopping_cart.views import OrderViewSet, CartViewSet
from custom_user.views import UsersViewSet
from django.urls import path, include

base_router = routers.DefaultRouter()
base_router.register('users', UsersViewSet, basename='users')

base_router.register(r'bakeries', BakeryViewSet)
base_router.register(r'ingredients', IngredientViewSet)
base_router.register(r'bakery_types', BakeryTypeViewSet)

users_router = routers.NestedSimpleRouter(base_router, r'users', lookup='user')
users_router.register(r'orders', OrderViewSet, basename='orders')

orders_router = routers.NestedSimpleRouter(users_router, r'orders', lookup='order')
orders_router.register(r'items', CartViewSet, basename='items')

urlpatterns = [
    path('', include(base_router.urls)),
    path('', include(users_router.urls)),
    path('', include(orders_router.urls)),
]
