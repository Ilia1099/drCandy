import factory
from customers.models import Customers, CustomerProfile


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customers

    mobile_number = "1234567890"
    email = factory.Faker("email")
    is_active = True


class CustomerProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomerProfile

    customer_id = factory.SubFactory(CustomerFactory)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    profile_img = factory.Faker("image_url")
    date_of_birth = factory.Faker(
        "date_between",
        start_date="-12y",
        end_date="-11y",
        # date_format="%m/%d/%Y"
    )

# TODO
# start working on apis
