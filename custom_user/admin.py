from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from custom_user.models import User, CustomerProfile


class CustomerAdmin(admin.ModelAdmin):
    model = User


class CustomerProfileAdmin(admin.ModelAdmin):
    model = CustomerProfile


admin.site.register(User, UserAdmin)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
