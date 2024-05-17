from django.contrib import admin
from .models import Order, Cart


class OrderAdmin(admin.ModelAdmin):
    model = Order


class CartAdmin(admin.ModelAdmin):
    model = Cart


admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)

