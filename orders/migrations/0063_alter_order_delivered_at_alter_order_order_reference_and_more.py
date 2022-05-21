# Generated by Django 4.0.3 on 2022-05-11 10:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0062_remove_order_itemss_alter_order_delivered_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_reference',
            field=models.UUIDField(default=uuid.UUID('e8dfda21-3b7a-46b8-bca5-b74012399e6d')),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]