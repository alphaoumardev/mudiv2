# Generated by Django 4.0.3 on 2022-05-09 05:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0075_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('ff9a799b-6bc5-4370-a5b5-d9b598867c3d')),
        ),
    ]
