# Generated by Django 4.0.3 on 2022-05-11 15:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0091_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('bbc50f06-7db9-4e43-9e15-9c2654be3416')),
        ),
    ]
