# Generated by Django 5.1.6 on 2025-02-17 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='effective_dose',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Effective Dose'),
        ),
        migrations.AlterField(
            model_name='drug',
            name='generic_code',
            field=models.CharField(max_length=50, verbose_name='Generic Code'),
        ),
        migrations.AlterField(
            model_name='drug',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Drug Name'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='national_id',
            field=models.CharField(max_length=50, unique=True, verbose_name='National ID'),
        ),
    ]
