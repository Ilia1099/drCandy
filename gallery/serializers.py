from rest_framework import serializers
from .models import Bakery, BakeryType, Ingredient


class BakeryTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakeryType
        fields = ['id', 'bakery_type', 'date_added', 'date_updated']
        read_only_fields = ['id', 'bakery_type', 'date_added', 'date_updated']


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'description', 'date_added', 'date_updated']
        read_only_fields = ['id', 'name', 'description', 'date_added', 'date_updated']


class BakerySerializer(serializers.ModelSerializer):
    ingredients = serializers.SerializerMethodField()

    def get_ingredients(self, obj):
        ingredients = obj.ingredients_set.all()
        serializer = IngredientsSerializer(ingredients, many=True)
        return serializer.data

    class Meta:
        model = Bakery
        fields = ['id', 'bakery_name', 'bakery_type_id', 'ingredients', 'description', 'ingredients', 'image',
                  'date_added', 'date_updated']
        read_only_fields = ['id', 'bakery_name', 'bakery_type_id', 'image', 'date_added', 'date_updated']

# TODO
# rework queries in all views (or serializers) which have related objects
# test existing endpoints
# add authentication, authorization
