# Generated by Django 3.2.25 on 2024-05-14 12:23

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SPV_app', '0004_alter_staff_requisition_which'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conditions_of_employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hired', models.CharField(max_length=2)),
                ('Type_of_Contract', models.CharField(max_length=100)),
                ('Overtime_Hours', models.CharField(max_length=2)),
                ('Duration_of_Engagement', models.DateField(default=datetime.date(2025, 5, 14))),
                ('Management_and_Trust', models.CharField(max_length=2)),
                ('Workplace', models.CharField(max_length=100)),
                ('Start_Date', models.DateField(default=django.utils.timezone.now)),
                ('Monday_to_Friday_start', models.TimeField(default=datetime.time(7, 0))),
                ('Monday_to_Friday_end', models.TimeField(default=datetime.time(17, 0))),
                ('Saturday_start', models.TimeField(default=datetime.time(7, 0))),
                ('Saturday_end', models.TimeField(default=datetime.time(17, 0))),
            ],
        ),
        migrations.CreateModel(
            name='Human_Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Identification_document', models.IntegerField()),
                ('Adress', models.CharField(max_length=100)),
                ('Phone_number', models.IntegerField(blank=True, null=True)),
                ('Movile_number', models.IntegerField()),
                ('Current_HIP', models.CharField(max_length=100)),
                ('AFP', models.CharField(max_length=100)),
                ('RH', models.CharField(max_length=3)),
                ('Allergies', models.CharField(blank=True, max_length=100, null=True)),
                ('Yellow_fever', models.CharField(max_length=100)),
                ('Tetanus', models.CharField(max_length=100)),
                ('Medical_examination', models.CharField(max_length=100)),
                ('Does_the_applicant_meet_the_job_profile', models.CharField(max_length=100)),
                ('Pants', models.IntegerField()),
                ('Shirt', models.CharField(max_length=2)),
                ('Shoes', models.IntegerField()),
                ('Overall', models.CharField(max_length=2)),
                ('Observations', models.TextField(blank=True, null=True)),
                ('Work_References', models.TextField(blank=True, null=True)),
                ('Personal_References', models.TextField()),
            ],
        ),
    ]
