# Generated by Django 4.0.3 on 2022-07-16 16:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0082_alter_useraccount_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email_verified',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('403ca003-9b39-4f02-8b65-285c2e5640ae'), primary_key=True, serialize=False, unique=True),
        ),
    ]
