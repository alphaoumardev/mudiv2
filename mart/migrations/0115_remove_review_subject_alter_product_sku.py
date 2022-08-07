# Generated by Django 4.0.3 on 2022-07-15 15:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0114_alter_review_options_remove_review_deleted_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='subject',
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('c21503ff-475e-4ae5-8c4e-7b0b6bdf7bd1')),
        ),
    ]
