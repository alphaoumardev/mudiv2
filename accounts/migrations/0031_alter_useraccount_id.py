# Generated by Django 4.0.3 on 2022-05-07 06:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_alter_useraccount_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a38e2482-4ff1-4c5b-aa24-38f85caf9a1d'), primary_key=True, serialize=False, unique=True),
        ),
    ]
