from django.contrib import admin

from custom_user.models import User, CustomerProfile


class CustomerAdmin(admin.ModelAdmin):
    model = User


class CustomerProfileAdmin(admin.ModelAdmin):
    model = CustomerProfile


admin.site.register(User, CustomerAdmin)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
