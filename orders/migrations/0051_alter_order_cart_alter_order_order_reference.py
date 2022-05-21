# Generated by Django 4.0.3 on 2022-05-07 12:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0050_remove_orderitem_added_at_remove_orderitem_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.cartitem'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_reference',
            field=models.UUIDField(default=uuid.UUID('c1289435-c3d4-4113-8074-f6f7ec044ac9')),
        ),
    ]