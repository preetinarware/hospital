# Generated by Django 3.2.7 on 2021-12-10 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billings',
            name='time',
        ),
        migrations.RemoveField(
            model_name='medical_records',
            name='time',
        ),
        migrations.RemoveField(
            model_name='prescriptions',
            name='time',
        ),
    ]
