# Generated by Django 5.1 on 2024-08-16 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='General_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('License_plate', models.CharField(max_length=7)),
                ('Class', models.CharField(max_length=50)),
                ('Engine_number', models.CharField(max_length=50)),
                ('Chassis_number', models.CharField(max_length=50)),
                ('Brand', models.CharField(max_length=50)),
                ('Model', models.IntegerField()),
                ('Sevice', models.CharField(max_length=50)),
                ('Owner', models.CharField(max_length=50)),
                ('Line', models.CharField(max_length=50)),
                ('Body', models.CharField(max_length=50)),
                ('Color', models.CharField(max_length=50)),
                ('Docment', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Docments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Diving_license', models.CharField(max_length=50)),
                ('Registration', models.CharField(max_length=50)),
                ('Gas_sistem_inspection', models.CharField(max_length=50)),
                ('SOAT', models.CharField(max_length=50)),
                ('Validity_SOAT', models.DateField(blank=True, null=True)),
                ('Tecno_mechanical', models.DateField(blank=True, null=True)),
                ('Operatin_card', models.CharField(max_length=50)),
                ('Operator', models.CharField(max_length=50)),
                ('Vehicle_insurance', models.CharField(max_length=50)),
                ('Policy_number', models.IntegerField(blank=True, null=True)),
                ('Vality_Inssurance', models.DateField(blank=True, null=True)),
                ('Front_photo', models.ImageField(upload_to='photos_vehicle/')),
                ('Side_photo', models.ImageField(upload_to='photos_vehicle/')),
                ('id_License_plate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hoja_de_vida_vehiculo.general_data')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnical_specifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fuel', models.CharField(max_length=50)),
                ('Drivetrain', models.CharField(max_length=50)),
                ('Displacement', models.IntegerField()),
                ('Drive_type', models.CharField(max_length=50)),
                ('Tires', models.CharField(max_length=50)),
                ('Load_capacity', models.CharField(max_length=100)),
                ('Air_conditioning', models.CharField(max_length=50)),
                ('Anti_lock_Braking_system', models.CharField(max_length=50)),
                ('Electronic_Brake_Distribution', models.CharField(max_length=50)),
                ('Brake_assist', models.CharField(max_length=50)),
                ('Third_brake_light', models.CharField(max_length=50)),
                ('Side_steps', models.CharField(max_length=50)),
                ('Airbag', models.CharField(max_length=50)),
                ('Fog_lights', models.CharField(max_length=50)),
                ('Central_locking', models.CharField(max_length=50)),
                ('Seat_covers', models.CharField(max_length=50)),
                ('Radio', models.CharField(max_length=50)),
                ('Power_windows', models.CharField(max_length=50)),
                ('General_observatios', models.TextField(blank=True, null=True)),
                ('id_License_plate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hoja_de_vida_vehiculo.general_data')),
            ],
        ),
    ]
