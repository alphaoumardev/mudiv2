# Generated by Django 4.0.3 on 2022-05-11 13:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0049_alter_useraccount_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3017321a-d78e-4b4d-9529-cc40bcd5f505'), primary_key=True, serialize=False, unique=True),
        ),
    ]