from rest_framework import viewsets
from rest_framework.generics import mixins
from .models import Bakery, BakeryType, Ingredient
from .serializers import BakerySerializer, BakeryTypesSerializer, IngredientsSerializer


class BakeryViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """A viewset retrieves for reading either a list of Bakery objects or a single Bakery object """

    lookup_field = 'id'
    queryset = Bakery.objects.prefetch_related("ingredients_set").all()
    serializer_class = BakerySerializer

    def get_queryset(self):
        qs = self.queryset
        if self.kwargs.get('id'):
            qs = Bakery.objects.filter(id=self.kwargs["id"])
        return qs


class IngredientViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """A viewset retrieves for reading either a list of Ingredient objects or a single Ingredient object """
    lookup_field = 'name'
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer


class BakeryTypeViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin):
    """A viewset retrieves for reading either a list of Bakery Type objects or a single object """
    lookup_field = 'bakery_type'
    queryset = BakeryType.objects.all()
    serializer_class = BakeryTypesSerializer

