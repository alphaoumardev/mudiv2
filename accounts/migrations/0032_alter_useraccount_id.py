# Generated by Django 4.0.3 on 2022-05-07 09:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_alter_useraccount_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('754e2404-ecbf-4651-9719-2378d8ad289c'), primary_key=True, serialize=False, unique=True),
        ),
    ]