# Generated by Django 4.0.3 on 2022-04-08 09:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0005_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('1f8bf99c-b837-4966-a6c5-8fc9b9607b27')),
        ),
    ]
