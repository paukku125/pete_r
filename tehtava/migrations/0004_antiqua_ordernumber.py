# Generated by Django 3.1.6 on 2021-08-04 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tehtava', '0003_auto_20210804_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='antiqua',
            name='orderNumber',
            field=models.IntegerField(null=True),
        ),
    ]
