from rest_framework.routers import DefaultRouter
from gallery.views import BakeryViewSet, IngredientViewSet, BakeryTypeViewSet

router = DefaultRouter()
router.register(r'bakery', BakeryViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'bakery_types', BakeryTypeViewSet)
