# Generated by Django 4.0.3 on 2022-05-13 10:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0066_alter_useraccount_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8b207d0e-f3b2-45f8-af7a-eb31bf5c4df0'), primary_key=True, serialize=False, unique=True),
        ),
    ]