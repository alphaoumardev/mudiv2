# Generated by Django 4.0.3 on 2022-05-11 13:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0089_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('9394c2b9-d689-4ec6-a37b-faf585c06801')),
        ),
    ]