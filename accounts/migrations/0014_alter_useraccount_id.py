# Generated by Django 4.0.3 on 2022-05-01 00:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_useraccount_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('fd085d6f-5507-4f58-a638-bc97f9193a72'), primary_key=True, serialize=False, unique=True),
        ),
    ]
