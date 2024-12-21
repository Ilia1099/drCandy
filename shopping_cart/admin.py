from django.contrib import admin
from .models import Order, CartItem


class OrderAdmin(admin.ModelAdmin):
    model = Order


class CartAdmin(admin.ModelAdmin):
    model = CartItem


admin.site.register(Order, OrderAdmin)
admin.site.register(CartItem, CartAdmin)

