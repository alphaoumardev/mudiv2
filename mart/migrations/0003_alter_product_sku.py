# Generated by Django 4.0.3 on 2022-04-08 08:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0002_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('55672e87-90ee-4c03-8723-aa1c2673ab8e')),
        ),
    ]
