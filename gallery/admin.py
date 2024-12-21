from django.contrib import admin
from .models import Bakery, BakeryType, Ingredient


class BakeryAdmin(admin.ModelAdmin):
    model = Bakery


class BakeryTypesAdmin(admin.ModelAdmin):
    model = BakeryType


class IngredientsAdmin(admin.ModelAdmin):
    model = Ingredient


admin.site.register(Bakery, BakeryAdmin)
admin.site.register(BakeryType, BakeryTypesAdmin)
admin.site.register(Ingredient, IngredientsAdmin)

