# Generated by Django 4.0.3 on 2022-04-30 14:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_useraccount_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('24460751-4d92-4d56-8ae4-aaf1b14deb57'), primary_key=True, serialize=False),
        ),
    ]