# Generated by Django 4.0.3 on 2022-05-12 14:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0063_alter_useraccount_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.UUID('df25d965-e50b-4a41-b6be-0823dca5fe29'), primary_key=True, serialize=False, unique=True),
        ),
    ]
