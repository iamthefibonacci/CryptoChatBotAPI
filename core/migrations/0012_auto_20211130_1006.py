# Generated by Django 3.2.8 on 2021-11-30 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20211130_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentimentdata',
            name='date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 11, 30, 10, 6, 26, 294578)),
        ),
        migrations.AlterField(
            model_name='sentimentdata',
            name='sum',
            field=models.FloatField(null=True),
        ),
    ]
