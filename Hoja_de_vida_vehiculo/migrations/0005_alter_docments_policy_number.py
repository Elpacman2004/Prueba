# Generated by Django 3.2.25 on 2024-05-28 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hoja_de_vida_vehiculo', '0004_auto_20240528_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docments',
            name='Policy_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
