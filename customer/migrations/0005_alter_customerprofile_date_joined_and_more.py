# Generated by Django 4.0.3 on 2022-04-08 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_customerprofile_avatar_customerprofile_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='last login'),
        ),
    ]