# Generated by Django 3.2.7 on 2021-12-27 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_pharmacy', '0006_alter_supplier_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='supplir',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='Admin_pharmacy.supplier'),
        ),
    ]