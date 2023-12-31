# Generated by Django 4.2.3 on 2023-07-06 10:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nationalId', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='just numbers Up to 10 digits allowed.', regex='^\\+?1?\\d{10,10}$')])),
                ('address', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('avatar', models.ImageField(upload_to='')),
                ('licence', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_type',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_driver',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.driverinfo'),
        ),
    ]
