# Generated by Django 4.0.3 on 2022-05-02 03:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0064_alter_category_options_alter_comments_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('9544b860-0665-46e1-a91e-656c60f6a286')),
        ),
    ]
