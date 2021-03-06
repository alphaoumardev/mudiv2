# Generated by Django 4.0.3 on 2022-05-01 03:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0037_alter_cartitem_id_alter_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7479492b-9e5f-455f-9490-d8e37290d5fc'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8ff33def-f3d2-49d4-9953-bc2760940e8c'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_reference',
            field=models.UUIDField(default=uuid.UUID('8ec9874f-017c-4889-b4bf-12e1ace18406')),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6b734ea5-a60a-44bf-a169-7b9bf6493475'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='id',
            field=models.UUIDField(default=uuid.UUID('55044c7a-1f7d-4886-93a1-41fa2663feb9'), primary_key=True, serialize=False),
        ),
    ]
