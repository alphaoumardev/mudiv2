# Generated by Django 4.0.3 on 2022-05-14 21:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0103_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('ae0d938d-c22a-44c2-bf80-356da7da36e5')),
        ),
    ]
