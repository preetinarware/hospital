# Generated by Django 3.2.7 on 2021-12-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_auto_20211210_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_record',
            name='mobile',
            field=models.IntegerField(blank=True),
        ),
    ]