# Generated by Django 4.0.3 on 2022-05-15 10:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0085_remove_order_products_alter_order_order_reference_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_reference',
            field=models.UUIDField(default=uuid.UUID('b69a93f7-2d8a-4127-824c-b86e1acb1c40')),
        ),
    ]
