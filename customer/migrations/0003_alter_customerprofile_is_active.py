# Generated by Django 4.0.3 on 2022-04-08 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customerprofile_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
