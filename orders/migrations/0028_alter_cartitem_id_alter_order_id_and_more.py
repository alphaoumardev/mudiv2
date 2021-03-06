# Generated by Django 4.0.3 on 2022-04-30 15:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0027_alter_cartitem_id_alter_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b8c771a0-6dc1-4e0b-8883-6fb40fb99412'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8c1dabbd-3b6b-4b96-aaa4-8d7d8a631aa7'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_reference',
            field=models.UUIDField(default=uuid.UUID('975ff1c5-bfa0-4574-aa06-989b8de4b43d')),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4ee545e3-6d4f-45ae-a19c-9bfa1c0fcc76'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='id',
            field=models.UUIDField(default=uuid.UUID('479fda3a-b62e-4ac2-be8f-f0d42ce0cf39'), primary_key=True, serialize=False),
        ),
    ]
