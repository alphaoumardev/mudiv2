# Generated by Django 4.0.3 on 2022-05-11 13:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0068_remove_order_cart_order_cart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ManyToManyField(blank=True, to='orders.orderitem'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_reference',
            field=models.UUIDField(default=uuid.UUID('ab6db919-786c-44fe-84e5-b1483d8f2743')),
        ),
    ]
