# Generated by Django 3.2.25 on 2024-06-11 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SPV_app', '0004_alter_conditions_of_employment_duration_of_engagement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conditions_of_employment',
            name='Duration_of_Engagement',
            field=models.DateField(default=datetime.date(2025, 6, 11)),
        ),
    ]
