# Generated by Django 3.2.25 on 2024-08-16 18:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DFAD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Equipment_description', models.TextField()),
                ('Photograph', models.ImageField(upload_to='Fotos de dispositivos')),
                ('Observations', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralDataDV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameD', models.CharField(max_length=100)),
                ('Brand', models.CharField(max_length=100)),
                ('Acquisition_Date', models.DateField()),
                ('Supply_Voltage', models.CharField(max_length=100)),
                ('RefModel', models.CharField(max_length=100)),
                ('Supplier', models.CharField(max_length=100)),
                ('Serial_number', models.CharField(max_length=100)),
                ('Invoice', models.CharField(max_length=100)),
                ('Type_device', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IMC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(default=django.utils.timezone.now)),
                ('Activity_description', models.CharField(max_length=100)),
                ('Activity_type', models.CharField(max_length=100)),
                ('Certificate_docment_number', models.CharField(max_length=100)),
                ('Satisfactory_result', models.CharField(max_length=100)),
                ('Action_to_take', models.CharField(max_length=100)),
                ('Next_revew', models.DateField()),
                ('Frequency', models.CharField(max_length=100)),
                ('Responsible', models.CharField(max_length=100)),
                ('Device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Testing_devices_app.generaldatadv')),
            ],
        ),
    ]
