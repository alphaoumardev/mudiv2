# Generated by Django 4.0.3 on 2022-05-08 08:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0054_alter_order_order_reference_and_more'),
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
            field=models.UUIDField(default=uuid.UUID('e13a4dc7-ddd1-4e78-96fe-c9a3eb269900')),
        ),
    ]