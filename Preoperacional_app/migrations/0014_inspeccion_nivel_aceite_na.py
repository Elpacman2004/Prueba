# Generated by Django 3.2.25 on 2024-04-15 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Preoperacional_app', '0013_rename_nive_aceite_inspeccion_nivel_aceite'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspeccion',
            name='Nivel_aceite_NA',
            field=models.BooleanField(default=False),
        ),
    ]