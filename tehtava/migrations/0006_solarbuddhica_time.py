# Generated by Django 3.1.6 on 2021-08-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tehtava', '0005_solarbuddhica_vaccinations_zerpfy'),
    ]

    operations = [
        migrations.AddField(
            model_name='solarbuddhica',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]