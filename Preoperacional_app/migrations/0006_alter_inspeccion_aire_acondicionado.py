# Generated by Django 3.2.25 on 2024-04-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Preoperacional_app', '0005_alter_inspeccion_aire_acondicionado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspeccion',
            name='aire_acondicionado',
            field=models.CharField(default='No Data', max_length=250, null=True),
        ),
    ]
