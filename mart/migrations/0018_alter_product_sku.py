# Generated by Django 4.0.3 on 2022-04-16 07:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0017_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('03983142-660b-4b1f-befe-e3e44829d1c1')),
        ),
    ]