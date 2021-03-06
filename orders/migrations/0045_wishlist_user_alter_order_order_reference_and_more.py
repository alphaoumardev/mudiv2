# Generated by Django 4.0.3 on 2022-05-02 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0044_alter_order_order_reference_alter_shippingaddress_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_reference',
            field=models.UUIDField(default=uuid.UUID('ac0e0e72-1beb-43c7-a4e8-3b0dae8bb1f9')),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='id',
            field=models.UUIDField(default=uuid.UUID('51c79752-a8c3-4b1d-9c9e-9c412b3b5a02'), primary_key=True, serialize=False),
        ),
    ]
