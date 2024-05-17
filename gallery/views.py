from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import mixins
from rest_framework.response import Response
from .models import Bakery, BakeryDescriptions, BakeryTypes, Ingredients
from .serializers import BakerySerializer, BakeryTypesSerializer, BakeryDescriptionsSerializer, IngredientsSerializer


class BakeryViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """A viewset retrieves for reading either a list of Bakery objects or a single Bakery object """

    lookup_field = 'id'
    queryset = Bakery.objects.all()
    serializer_class = BakerySerializer
