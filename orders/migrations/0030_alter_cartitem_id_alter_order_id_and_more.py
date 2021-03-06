# Generated by Django 4.0.3 on 2022-05-01 00:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0029_alter_cartitem_id_alter_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bdd4cf11-5c7c-49f9-8bbd-2af102cbb54b'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8a4ea31b-367c-4aad-827f-78a49b01f0d6'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_reference',
            field=models.UUIDField(default=uuid.UUID('031dafe7-08a9-4f18-b42f-dceb76c427ed')),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4e03bff2-0380-4acf-a03f-0e9f1fb54b2d'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2b4031de-6058-4458-bc75-84a57b60a368'), primary_key=True, serialize=False),
        ),
    ]
