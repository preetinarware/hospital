# Generated by Django 3.2.7 on 2021-12-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy_admin_record',
            name='dob',
            field=models.DateField(blank=True),
        ),
    ]
