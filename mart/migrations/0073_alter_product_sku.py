# Generated by Django 4.0.3 on 2022-05-08 08:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0072_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('30643b12-0d72-43f1-a9e5-61da3b0e3bbe')),
        ),
    ]