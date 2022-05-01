# Generated by Django 4.0.3 on 2022-04-30 14:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0042_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b742f54b-6aa2-4a64-88de-9f76ba900f06'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='futuredimages',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6a172056-ff93-429b-9e5d-6bede66e9728'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2f597263-ee52-408e-b395-155790b49b65'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('6b575e93-10d5-4034-9cb1-03347c952bf0')),
        ),
        migrations.AlterField(
            model_name='variant',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a618fec6-8c82-4a9c-a7e6-b61cc0fe9d2d'), primary_key=True, serialize=False),
        ),
    ]
