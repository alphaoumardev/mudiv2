# Generated by Django 4.0.3 on 2022-04-17 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_useraccount_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='city',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='country',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='detailed_address',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='state_or_province',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='zip_code',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.EmailField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='first_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='last_name',
            field=models.CharField(max_length=25),
        ),
    ]
