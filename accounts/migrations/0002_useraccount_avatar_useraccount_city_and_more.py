# Generated by Django 4.0.3 on 2022-04-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='mudi'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='city',
            field=models.CharField(default='Najing', max_length=20),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='country',
            field=models.CharField(default='China', max_length=10),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='detailed_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Secret', 'Secret')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='state_or_province',
            field=models.CharField(default='Jiangsu', max_length=20),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='zip_code',
            field=models.IntegerField(default=210010),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='last_login',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='last login'),
        ),
    ]
