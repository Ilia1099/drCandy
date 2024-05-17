from django.contrib import admin

from customers.models import Customers, CustomerProfile


class CustomerAdmin(admin.ModelAdmin):
    model = Customers


class CustomerProfileAdmin(admin.ModelAdmin):
    model = CustomerProfile


admin.site.register(Customers, CustomerAdmin)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
