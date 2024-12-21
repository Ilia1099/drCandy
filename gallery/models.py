from django.db import models
from treebeard.mp_tree import MP_Node


class BakeryType(MP_Node):
    """ A model for bakery types instances"""
    bakery_type = models.TextField(max_length=255, db_index=True, null=True, blank=True, unique=True, default='')
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.bakery_type

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = "bakery_type"
        verbose_name = 'Bakery Type'
        verbose_name_plural = 'Bakery Types'
        db_table_comment = "Table with all bakery types"


class Bakery(models.Model):
    """ A model for bakery instances"""
    bakery_name = models.TextField(max_length=255, db_index=True)
    bakery_type_id = models.ForeignKey(to="BakeryType", on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="bakery_images", null=True, default=None)
    description = models.TextField(null=True, blank=False, unique=True)
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.description:
            self.description = f"{self.bakery_name}'s description"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.bakery_name

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = "bakery"
        verbose_name = 'Bakery'
        verbose_name_plural = 'Bakeries'
        db_table_comment = "Table with all bakeries"


class Ingredient(models.Model):
    """ A model for ingredients instances """
    name = models.TextField(max_length=50, db_index=True, null=False, blank=False)
    bakery_id = models.ManyToManyField(to="Bakery")
    description = models.TextField(null=False, blank=False)
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = 'ingredient'
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
        db_table_comment = "Table with all ingredients"
