# Generated by Django 4.0.3 on 2022-05-11 15:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0095_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('5a929df2-bf7d-441e-8387-4e4c31c694ab')),
        ),
    ]
