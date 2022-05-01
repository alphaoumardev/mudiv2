# Generated by Django 4.0.3 on 2022-04-30 14:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_alter_cartitem_user_alter_order_order_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.UUIDField(default=uuid.UUID('92f3a644-36ab-4979-8c92-6a398c65b151'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.UUID('690f448d-d341-4326-8418-97a174d67bb6'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_reference',
            field=models.UUIDField(default=uuid.UUID('31341ad3-b3c4-4124-83b1-c69a31e5c1a8')),
        ),
    ]