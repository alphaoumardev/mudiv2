# Generated by Django 4.0.3 on 2022-05-01 02:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_useraccount_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('234abd9f-1e83-4336-8b0c-619ca97ba566'), primary_key=True, serialize=False, unique=True),
        ),
    ]
