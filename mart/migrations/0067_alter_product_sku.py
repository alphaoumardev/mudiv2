# Generated by Django 4.0.3 on 2022-05-07 09:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0066_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('bc0030e9-2292-45c7-a74f-95d30305100e')),
        ),
    ]
