from rest_framework.routers import DefaultRouter
from gallery.views import BakeryViewSet

router = DefaultRouter()
router.register(r'bakery', BakeryViewSet)
