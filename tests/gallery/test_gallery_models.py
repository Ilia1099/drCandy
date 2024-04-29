import pytest

pytestmark = pytest.mark.django_db


class TestGalleryModels:
    def test_bakery_types(self, bakery_type_factory):
        bakery_type = bakery_type_factory()
        assert bakery_type.__str__() == bakery_type.bakery_type
        assert bakery_type.__repr__() == bakery_type.bakery_type

    def test_bakery(self, bakery_factory):
        bakery = bakery_factory()
        assert bakery.__str__() == bakery.bakery_name
        assert bakery.__repr__() == bakery.bakery_name

    def test_description(self, description_factory):
        description = description_factory()
        assert description.__str__() == "description"
        assert description.__repr__() == "description"

    def test_ingredients(self, ingredients_factory):
        ingredients = ingredients_factory()
        assert ingredients.__str__() == ingredients.name
        assert ingredients.__repr__() == ingredients.name
