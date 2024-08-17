from django.contrib import admin
from .models import Order, CartItems


class OrderAdmin(admin.ModelAdmin):
    model = Order


class CartAdmin(admin.ModelAdmin):
    model = CartItems


admin.site.register(Order, OrderAdmin)
admin.site.register(CartItems, CartAdmin)

