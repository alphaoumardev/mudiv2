# Generated by Django 4.0.3 on 2022-05-15 10:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0104_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('2f7967be-2e4d-4dc7-ba90-93abdddee936')),
        ),
    ]
