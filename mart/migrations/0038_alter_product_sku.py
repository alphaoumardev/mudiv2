# Generated by Django 4.0.3 on 2022-04-29 00:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0037_rename_product_sliders_slideitem_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('5321b37a-3c69-4b28-9c30-ff0069b5af4e')),
        ),
    ]