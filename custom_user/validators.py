from django.core.exceptions import ValidationError


def mobile_number_validator(value):
    if len(value) != 10:
        raise ValidationError("Mobile Number must be 10 digits long")