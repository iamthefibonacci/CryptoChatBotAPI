# Generated by Django 3.2.8 on 2021-11-30 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20211130_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentimentdata',
            name='date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 11, 30, 9, 54, 23, 192693)),
        ),
    ]