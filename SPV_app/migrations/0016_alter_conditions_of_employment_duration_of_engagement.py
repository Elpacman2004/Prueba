# Generated by Django 3.2.25 on 2024-09-26 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SPV_app', '0015_alter_conditions_of_employment_duration_of_engagement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conditions_of_employment',
            name='Duration_of_Engagement',
            field=models.DateField(default=datetime.date(2025, 9, 26)),
        ),
    ]