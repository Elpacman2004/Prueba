# Generated by Django 3.2.25 on 2024-04-17 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Preoperacional_app', '0002_auto_20240417_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inspeccion',
            name='Nivel_aceite_NA',
        ),
        migrations.RemoveField(
            model_name='inspeccion',
            name='capot_asegurado_NA',
        ),
        migrations.AlterField(
            model_name='inspeccion',
            name='Nivel_aceite',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='inspeccion',
            name='capot_asegurado',
            field=models.CharField(max_length=250),
        ),
    ]