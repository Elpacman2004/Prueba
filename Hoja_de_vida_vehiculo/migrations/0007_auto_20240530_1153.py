# Generated by Django 3.2.25 on 2024-05-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hoja_de_vida_vehiculo', '0006_auto_20240528_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tecnical_specifications',
            old_name='Engine',
            new_name='Drivetrain',
        ),
        migrations.AddField(
            model_name='tecnical_specifications',
            name='Fuel',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
