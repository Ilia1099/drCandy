from rest_framework.routers import DefaultRouter
from gallery.views import BakeryViewSet, IngredientViewSet, BakeryTypeViewSet
from shopping_cart.views import OrderViewSet, CartViewSet

router = DefaultRouter()
router.register(r'bakeries', BakeryViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'bakery_types', BakeryTypeViewSet)
router.register(r'order_items', CartViewSet)
router.register(r'orders', OrderViewSet)
