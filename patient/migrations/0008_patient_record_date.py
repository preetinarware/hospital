# Generated by Django 3.2.7 on 2021-12-12 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_alter_patient_record_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_record',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
