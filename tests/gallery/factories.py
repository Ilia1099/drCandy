import factory
from gallery import models


class BakeryTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BakeryTypes

    bakery_type = factory.Faker('text', max_nb_chars=255)


class BakeryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Bakery

    bakery_name = factory.Faker('text', max_nb_chars=255)
    bakery_type_id = factory.SubFactory(BakeryTypeFactory)
    image = factory.Faker('url')


class DescriptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BakeryDescriptions

    bakery_id = factory.SubFactory(BakeryFactory)
    description = factory.Faker('text', max_nb_chars=255)


class IngredientsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Ingredients

    name = factory.Faker('text', max_nb_chars=50)
    bakery_id = factory.RelatedFactory(BakeryFactory)
    description = factory.Faker('text', max_nb_chars=255)
