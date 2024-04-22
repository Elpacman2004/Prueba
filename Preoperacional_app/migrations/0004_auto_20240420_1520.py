# Generated by Django 3.2.25 on 2024-04-20 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Preoperacional_app', '0003_auto_20240417_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspeccion',
            name='aire_acondicionado',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='aire_acondicionado_NC',
            field=models.ImageField(default=False, upload_to='Aire acondicionado'),
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='bornes_baterias_ajustados',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='bornes_baterias_ajustados_NC',
            field=models.ImageField(default=False, upload_to='Bornes baterias ajustados'),
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='botiquin_primeros_auxilios',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='botiquin_primeros_auxilios_NC',
            field=models.ImageField(default=False, upload_to='Botiquin primeros auxilios'),
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='cinturones_seguridad',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='cinturones_seguridad_NC',
            field=models.ImageField(default=False, upload_to='Cinturones seguridad'),
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='equipo_prevencion_seguridad',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='equipo_prevencion_seguridad_NC',
            field=models.ImageField(default=False, upload_to='Equipo prevencion seguridad'),
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='extintor',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='extintor_NC',
            field=models.ImageField(default=False, upload_to='Extintor'),
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='freno_estacionamiento',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='freno_estacionamiento_NC',
            field=models.ImageField(default=False, upload_to='Freno estacionamiento'),
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='indicadores_tablero_control',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='indicadores_tablero_control_NC',
            field=models.ImageField(default=False, upload_to='Indicadores tablero control'),
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='kit_carreteras',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='kit_carreteras_NC',
            field=models.ImageField(default=False, upload_to='Kit carreteras'),
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='limpiaparabrisas',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='limpiaparabrisas_NC',
            field=models.ImageField(default=False, upload_to='Limpiaparabrisas'),
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='pito_electrico',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='pito_electrico_NC',
            field=models.ImageField(default=False, upload_to='Pito electrico'),
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='sensor_externo_velocidad',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspeccion',
            name='sensor_externo_velocidad_NC',
            field=models.ImageField(default=False, upload_to='Sensor externo velocidad'),
        ),
    ]