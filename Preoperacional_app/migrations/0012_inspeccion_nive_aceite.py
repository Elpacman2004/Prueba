# Generated by Django 3.2.25 on 2024-04-15 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Preoperacional_app', '0011_auto_20240415_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspeccion',
            name='Nive_aceite',
            field=models.BooleanField(default=False),
        ),
    ]
