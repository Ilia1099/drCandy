from django.contrib.auth.forms import UserChangeForm, UsernameField
from django import forms
from .models import User, CustomerProfile, mobile_number_validator


class CustomUserChangeForm(UserChangeForm):
    """Form for changing user's data, inherits from UserChangeForm."""
    is_customer = forms.BooleanField(
        required=False,
        label="Customer status",

    )
    mobile_number = forms.CharField(
        validators=[mobile_number_validator],
        max_length=10,
        label="Mobile number",

    )

    class Meta:
        model = User
        fields = "__all__"
        field_classes = {"username": UsernameField}


class CustomerProfileForm(forms.ModelForm):
    """Form for changing user's profile data, under development"""
    class Meta:
        model = CustomerProfile
        fields = "__all__"
