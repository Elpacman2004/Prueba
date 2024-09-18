# Generated by Django 5.1 on 2024-08-16 14:52

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hoja_de_vida_vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('luces_traseras_funcionando', models.CharField(max_length=250)),
                ('sonido_alarma_reversa', models.CharField(max_length=250)),
                ('labrado_llantas_traseras', models.CharField(max_length=250)),
                ('labrado_llanta_repuesto', models.CharField(max_length=250)),
                ('placa_trasera_legible', models.CharField(max_length=250)),
                ('Obser', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FrontPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcionamiento_luces_delanteras', models.CharField(max_length=250)),
                ('vidrio_delantero_sin_fisuras', models.CharField(max_length=250)),
                ('placa_delantera_legible', models.CharField(max_length=250)),
                ('Labrado_de_las_llantas_delanteras', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nivel_aceite_NC', models.ImageField(default=False, upload_to='Nivel de aceite')),
                ('capot_asegurado_NC', models.ImageField(default=False, upload_to='Capot asegurado')),
                ('bornes_baterias_ajustados_NC', models.ImageField(default=False, upload_to='Bornes baterias ajustados')),
                ('indicadores_tablero_control_NC', models.ImageField(default=False, upload_to='Indicadores tablero control')),
                ('aire_acondicionado_NC', models.ImageField(default=False, upload_to='Aire acondicionado')),
                ('freno_estacionamiento_NC', models.ImageField(default=False, upload_to='Freno estacionamiento')),
                ('limpiaparabrisas_NC', models.ImageField(default=False, upload_to='Limpiaparabrisas')),
                ('pito_electrico_NC', models.ImageField(default=False, upload_to='Pito electrico')),
                ('cinturones_seguridad_NC', models.ImageField(default=False, upload_to='Cinturones seguridad')),
                ('equipo_prevencion_seguridad_NC', models.ImageField(default=False, upload_to='Equipo prevencion seguridad')),
                ('botiquin_primeros_auxilios_NC', models.ImageField(default=False, upload_to='Botiquin primeros auxilios')),
                ('extintor_NC', models.ImageField(default=False, upload_to='Extintor')),
                ('kit_carreteras_NC', models.ImageField(default=False, upload_to='Kit carreteras')),
                ('sensor_externo_velocidad_NC', models.ImageField(default=False, upload_to='Sensor externo velocidad')),
                ('funcionamiento_luces_delanteras_NC', models.ImageField(default=False, upload_to='funcionamiento de luces delanteras')),
                ('vidrio_delantero_sin_fisuras_NC', models.ImageField(default=False, upload_to='vidrio delantero sin fisuras')),
                ('placa_delantera_legible_NC', models.ImageField(default=False, upload_to='placa delantera legible')),
                ('Labrado_de_las_llantas_delanteras_NC', models.ImageField(default=False, upload_to='Labrado de las llantas delanteras')),
                ('carroceria_buen_estado_NC', models.ImageField(default=False, upload_to='carroceria en buen estado')),
                ('vidrios_laterales_sin_fisuras_NC', models.ImageField(default=False, upload_to='vidrios laterales sin fisuras')),
                ('direccionales_funcionando_NC', models.ImageField(default=False, upload_to='direccionales funcionando')),
                ('espejo_exterior_buen_estado_NC', models.ImageField(default=False, upload_to='espejo exterior buen estado')),
                ('sin_fugas_tanque_combustible', models.ImageField(default=False, upload_to='sin fugas tanque combustible')),
                ('luces_traseras_funcionando_NC', models.ImageField(default=False, upload_to='luces traseras funcionando')),
                ('sonido_alarma_reversa_NC', models.ImageField(default=False, upload_to='sonido alarma reversa')),
                ('labrado_llantas_traseras_NC', models.ImageField(default=False, upload_to='labrado de las llantas traseras')),
                ('labrado_llanta_repuesto_NC', models.ImageField(default=False, upload_to='labrado de la llanta repuesto')),
                ('placa_trasera_legible_NC', models.ImageField(default=False, upload_to='placa trasera legible')),
            ],
        ),
        migrations.CreateModel(
            name='Inspeccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('Nivel_aceite', models.CharField(max_length=250)),
                ('capot_asegurado', models.CharField(max_length=250)),
                ('bornes_baterias_ajustados', models.CharField(max_length=250)),
                ('indicadores_tablero_control', models.CharField(max_length=250)),
                ('kilometraje_inicial', models.IntegerField(default=0)),
                ('aire_acondicionado', models.CharField(max_length=250)),
                ('freno_estacionamiento', models.CharField(max_length=250)),
                ('limpiaparabrisas', models.CharField(max_length=250)),
                ('pito_electrico', models.CharField(max_length=250)),
                ('cinturones_seguridad', models.CharField(max_length=250)),
                ('equipo_prevencion_seguridad', models.CharField(max_length=250)),
                ('botiquin_primeros_auxilios', models.CharField(max_length=250)),
                ('extintor', models.CharField(max_length=250)),
                ('kit_carreteras', models.CharField(max_length=250)),
                ('sensor_externo_velocidad', models.CharField(max_length=250)),
                ('Nivel_del_combustible', models.ImageField(default=False, upload_to='Nivel gasometro')),
            ],
        ),
        migrations.CreateModel(
            name='Side',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carroceria_buen_estado', models.CharField(max_length=250)),
                ('vidrios_laterales_sin_fisuras', models.CharField(max_length=250)),
                ('direccionales_funcionando', models.CharField(max_length=250)),
                ('espejo_exterior_buen_estado', models.CharField(max_length=250)),
                ('sin_fugas_tanque_combustible', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Datos_generales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField(default=django.utils.timezone.now)),
                ('Proyecto', models.CharField(default='PP-000-0000', max_length=18)),
                ('Nombre', models.CharField(max_length=30)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hoja_de_vida_vehiculo.general_data')),
            ],
        ),
        migrations.CreateModel(
            name='File_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_path', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hoja_de_vida_vehiculo.general_data')),
            ],
        ),
    ]
