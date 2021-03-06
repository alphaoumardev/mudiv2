# Generated by Django 4.0.3 on 2022-05-11 16:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0077_remove_orderitem_order_orderitem_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ManyToManyField(blank=True, to='orders.cartitem'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_reference',
            field=models.UUIDField(default=uuid.UUID('4131a840-4da3-4fad-a533-eea35fe12383')),
        ),
    ]
