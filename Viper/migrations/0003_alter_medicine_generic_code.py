# Generated by Django 5.1.6 on 2025-02-17 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Viper', '0002_medicine_available_patientmedicine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='generic_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Generic Code'),
        ),
    ]
