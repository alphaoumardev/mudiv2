# Generated by Django 4.0.3 on 2022-04-08 08:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('56ac7d37-2a13-48b0-ab36-d25f97d9b283')),
        ),
    ]
