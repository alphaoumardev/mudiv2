# Generated by Django 4.0.3 on 2022-07-15 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mart', '0113_rename_comments_review_alter_product_sku'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name_plural': 'Reviews'},
        ),
        migrations.RemoveField(
            model_name='review',
            name='deleted_at',
        ),
        migrations.AddField(
            model_name='review',
            name='rate',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('18640570-67e2-4bab-b61a-a6deec8b9743')),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mart.product'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
