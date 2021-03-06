# Generated by Django 4.0.3 on 2022-05-01 02:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0053_alter_product_sku_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('ead281ee-b760-40d0-a67e-f974da694285')),
        ),
    ]
