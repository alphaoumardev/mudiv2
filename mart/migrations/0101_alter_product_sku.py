# Generated by Django 4.0.3 on 2022-05-12 16:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0100_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('4314d9f1-08e1-4c74-a887-e8ce97f8818e')),
        ),
    ]
