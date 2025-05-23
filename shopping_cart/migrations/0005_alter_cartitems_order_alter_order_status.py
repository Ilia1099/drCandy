# Generated by Django 5.0.4 on 2024-10-12 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shopping_cart.order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('c', 'Confirmed'), ('d', 'Delivered'), ('p', 'Pending'), ('rcd', 'Received'), ('r', 'Rejected'), ('a', 'Archived'), ('s', 'Suspended'), ('b', 'Basket'), ('prcg', 'Processing'), ('shpd', 'Shipping')], default='b', max_length=4),
        ),
    ]
