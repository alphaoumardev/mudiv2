# Generated by Django 4.0.3 on 2022-05-02 03:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0045_wishlist_user_alter_order_order_reference_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_reference',
            field=models.UUIDField(default=uuid.UUID('63f6a74c-3805-4b18-9390-cd93c4285d7f')),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
