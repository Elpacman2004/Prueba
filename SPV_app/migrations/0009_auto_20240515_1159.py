# Generated by Django 3.2.25 on 2024-05-15 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SPV_app', '0008_auto_20240515_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conditions_of_employment',
            name='Monday_to_Friday_start',
            field=models.TimeField(default=datetime.time(7, 0)),
        ),
        migrations.AlterField(
            model_name='conditions_of_employment',
            name='Saturday_start',
            field=models.TimeField(default=datetime.time(7, 0)),
        ),
    ]
