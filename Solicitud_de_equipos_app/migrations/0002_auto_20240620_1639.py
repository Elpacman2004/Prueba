# Generated by Django 3.2.25 on 2024-06-20 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Solicitud_de_equipos_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools_and_Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planta_electrica', models.IntegerField(verbose_name='PLANTA ELECTRICA')),
                ('juego_de_tierras', models.IntegerField(verbose_name='JUEGO DE TIERRAS')),
                ('caja_herramientas', models.IntegerField(verbose_name='CAJA DE HERRAMIENTAS')),
                ('pertiga_escopeta', models.IntegerField(verbose_name='PERTIGA ESCOPETA')),
                ('pertiga_telescopica', models.IntegerField(verbose_name='PERTIGA TELESCOPICA')),
                ('pistola_calor', models.IntegerField(verbose_name='PISTOLA DE CALOR')),
                ('motor_tool', models.IntegerField(verbose_name='MOTOR TOOL')),
                ('kit_soldadura_cautin', models.IntegerField(verbose_name='KIT DE SOLDADURA CAUTIN')),
                ('pistola_silicona', models.IntegerField(verbose_name='PISTOLA DE SILICONA')),
                ('sopladora', models.IntegerField(verbose_name='SOPLADORA')),
                ('taladro', models.IntegerField(verbose_name='TALADRO')),
                ('filtro_sf6', models.IntegerField(verbose_name='FILTRO SF6')),
                ('compresor_pintura', models.IntegerField(verbose_name='COMPRESOR PARA PINTURA')),
                ('compresor_aire_seco', models.IntegerField(verbose_name='COMPRESOR AIRE SECO')),
                ('equipo_soldadura', models.IntegerField(verbose_name='EQUIPO SOLDADURA')),
                ('radio_transmissor', models.IntegerField(verbose_name='RADIO TRANSMISSOR')),
                ('higrometro', models.IntegerField(verbose_name='HIGROMETRO')),
                ('pata_de_cabra', models.IntegerField(verbose_name='PATA DE CABRA')),
                ('ponchadora_hidraulica', models.IntegerField(verbose_name='PONCHADORA HIDRAULICA')),
                ('ponchadora_neumatica', models.IntegerField(verbose_name='PONCHADORA NEUMÁTICA')),
                ('cizalla_manual', models.IntegerField(verbose_name='BOMBA MANUAL')),
                ('tarrajero', models.IntegerField(verbose_name='TARRAJERO')),
                ('bomba_para_aceite', models.IntegerField(verbose_name='BOMBA PARA ACEITE')),
                ('pistola_pintura', models.IntegerField(verbose_name='PISTOLA DE PINTURA')),
                ('extension_electrica', models.IntegerField(verbose_name='EXTENSION ELECTRICA')),
                ('esmeril', models.IntegerField(verbose_name='ESMERIL')),
                ('sonda', models.IntegerField(verbose_name='SONDA')),
                ('kit_muestra_aceite', models.IntegerField(verbose_name='KIT MUESTRA DE ACEITE')),
                ('tarraja', models.IntegerField(verbose_name='TARRAJA')),
                ('aspiradora', models.IntegerField(verbose_name='ASPIRADORA')),
                ('pulidora', models.IntegerField(verbose_name='PULIDORA')),
                ('caladora', models.IntegerField(verbose_name='CALADORA')),
                ('reflector', models.IntegerField(verbose_name='REFLECTOR')),
                ('tijera_metal', models.IntegerField(verbose_name='TIJERA PARA METAL')),
                ('poleas', models.IntegerField(verbose_name='POLEAS')),
                ('maleta_sf6', models.IntegerField(verbose_name='MALETA MANGUERAS SF6')),
                ('maquina_filtroprensa', models.IntegerField(verbose_name='MAQUINA FILTROPRENSA')),
            ],
        ),
        migrations.DeleteModel(
            name='ToolsAndAccessories',
        ),
    ]
