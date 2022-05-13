# Generated by Django 4.0.3 on 2022-05-11 13:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0066_remove_order_cart_order_cartitem_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cartItem',
            new_name='cart',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_reference',
            field=models.UUIDField(default=uuid.UUID('8b179f13-da69-4b88-b6d0-bb6c63e49892')),
        ),
    ]
