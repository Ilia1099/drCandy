from rest_framework.routers import DefaultRouter
from gallery.views import BakeryViewSet, IngredientViewSet, BakeryTypeViewSet
from shopping_cart.views import OrderViewSet, CartViewSet

router = DefaultRouter()
router.register(r'bakery', BakeryViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'bakery_types', BakeryTypeViewSet)
router.register(r'shopping_cart', CartViewSet)
router.register(r'order', OrderViewSet)
