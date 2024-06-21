import factory
from custom_user.models import User, CustomerProfile


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.Faker('password')
    mobile_number = "1234567890"
    email = factory.Faker("email")
    is_active = True


class CustomerProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomerProfile

    customer_id = factory.SubFactory(CustomerFactory)
    profile_img = factory.Faker("image_url")
    date_of_birth = factory.Faker(
        "date_between",
        start_date="-12y",
        end_date="-11y",
    )

