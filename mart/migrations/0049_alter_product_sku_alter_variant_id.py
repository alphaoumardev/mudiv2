# Generated by Django 4.0.3 on 2022-05-01 00:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0048_alter_product_sku_alter_variant_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('07391159-7ebc-444d-bf5f-5a844ad470ce')),
        ),
        migrations.AlterField(
            model_name='variant',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]