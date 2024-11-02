from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from custom_user.models import User, CustomerProfile
from .forms import CustomUserChangeForm, CustomerProfileForm


class CustomUserAdmin(UserAdmin):
    """Model admin class to manage custom User model via admin page"""
    form = CustomUserChangeForm
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_customer")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "mobile_number")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_customer",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


class CustomerProfileAdmin(admin.ModelAdmin):
    """Model admin class to manage CustomerProfile model via admin page"""
    list_display = ("customer_id", "username",)
    model = CustomerProfile
    form = CustomerProfileForm

    def username(self, obj: CustomerProfile):
        return obj.customer_id.username


admin.site.register(User, CustomUserAdmin)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
