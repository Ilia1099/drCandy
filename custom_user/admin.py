from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from custom_user.models import User, CustomerProfile


class CustomerAdmin(admin.ModelAdmin):
    """this class is under development"""
    model = User


class CustomerProfileAdmin(admin.ModelAdmin):
    """this class is under development"""
    model = CustomerProfile


admin.site.register(User, UserAdmin)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
