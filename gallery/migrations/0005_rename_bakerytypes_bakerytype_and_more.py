# Generated by Django 5.0.4 on 2024-12-21 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_squashed_0004_alter_bakery_bakery_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BakeryTypes',
            new_name='BakeryType',
        ),
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
        migrations.AlterModelTable(
            name='bakerytype',
            table='bakery_type',
        ),
        migrations.AlterModelTable(
            name='ingredient',
            table='ingredient',
        ),
    ]
