# Generated by Django 4.0.3 on 2022-04-30 15:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_useraccount_id_alter_userprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('180fe8c2-5d88-4419-875e-b7552f4b055c'), primary_key=True, serialize=False, unique=True),
        ),
    ]