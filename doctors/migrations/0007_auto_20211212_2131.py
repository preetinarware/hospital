# Generated by Django 3.2.7 on 2021-12-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_rvw_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='dr',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dr',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
