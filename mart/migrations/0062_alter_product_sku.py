# Generated by Django 4.0.3 on 2022-05-01 04:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0061_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('0ca72abd-ee73-48e3-9191-23042d39677b')),
        ),
    ]