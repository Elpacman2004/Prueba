# Generated by Django 5.1 on 2024-09-17 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SPV_app', '0010_alter_conditions_of_employment_duration_of_engagement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conditions_of_employment',
            name='Duration_of_Engagement',
            field=models.DateField(default=datetime.date(2025, 9, 17)),
        ),
    ]