from django.contrib import admin
from .models import Bakery, BakeryDescriptions, BakeryTypes, Ingredients


class BakeryAdmin(admin.ModelAdmin):
    model = Bakery


class BakeryDescriptionsAdmin(admin.ModelAdmin):
    model = BakeryDescriptions


class BakeryTypesAdmin(admin.ModelAdmin):
    model = BakeryTypes


class IngredientsAdmin(admin.ModelAdmin):
    model = Ingredients


admin.site.register(Bakery, BakeryAdmin)
admin.site.register(BakeryDescriptions, BakeryDescriptionsAdmin)
admin.site.register(BakeryTypes, BakeryTypesAdmin)
admin.site.register(Ingredients, IngredientsAdmin)

