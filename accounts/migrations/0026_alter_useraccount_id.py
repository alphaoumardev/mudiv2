# Generated by Django 4.0.3 on 2022-05-01 03:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_alter_useraccount_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('96f8914c-f48a-4325-8f7d-3931c7d7e97f'), primary_key=True, serialize=False, unique=True),
        ),
    ]
