# Generated by Django 4.0.3 on 2022-05-08 09:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0074_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('54014aaf-f9d1-4212-b68a-a90ca9bd67b0')),
        ),
    ]