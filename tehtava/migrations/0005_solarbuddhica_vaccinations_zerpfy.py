# Generated by Django 3.1.6 on 2021-08-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tehtava', '0004_antiqua_ordernumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolarBuddhica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNumber', models.IntegerField(null=True)),
                ('personName', models.CharField(max_length=200, null=True)),
                ('healtCare', models.CharField(max_length=200, null=True)),
                ('injections', models.CharField(max_length=200, null=True)),
                ('arrived', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=200, null=True)),
                ('vaccinationDate', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zerpfy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNumber', models.IntegerField(null=True)),
                ('personName', models.CharField(max_length=200, null=True)),
                ('healtCare', models.CharField(max_length=200, null=True)),
                ('injections', models.CharField(max_length=200, null=True)),
                ('arrived', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
