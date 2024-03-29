# Generated by Django 4.0.3 on 2022-07-16 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0083_remove_userprofile_email_verified_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4818a421-858a-46bd-8fb3-d5423104fcd1'), primary_key=True, serialize=False, unique=True),
        ),
    ]
