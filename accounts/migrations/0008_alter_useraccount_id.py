# Generated by Django 4.0.3 on 2022-04-30 14:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_userprofile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('634db875-2832-4791-8dc1-6f4e00b1fb88'), primary_key=True, serialize=False),
        ),
    ]