# Generated by Django 5.1 on 2024-08-16 14:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmc_356_omicron', models.IntegerField(verbose_name='CMC 356 OMICRON')),
                ('cmc_353_omicron', models.IntegerField(verbose_name='CMC 353 OMICRON')),
                ('doble_f6150', models.IntegerField(verbose_name='DOBLE F6150')),
                ('ponovo_l336i', models.IntegerField(verbose_name='PONOVO L336i')),
                ('cpc_100_omicron', models.IntegerField(verbose_name='CPC 100 OMICRON')),
                ('cp_td1_omicron', models.IntegerField(verbose_name='CP-TD1 OMICRON')),
                ('cp_cu1_omicron', models.IntegerField(verbose_name='CP-CU1 OMICRON')),
                ('cp_cr500_omicron', models.IntegerField(verbose_name='CP-CR500 OMICRON')),
                ('ct_analyzer_omicron', models.IntegerField(verbose_name='CT-ANALYZER OMICRON')),
                ('franalizer_omicron', models.IntegerField(verbose_name='FRANALYZER OMICRON')),
                ('cp_cb2_omicron', models.IntegerField(verbose_name='CP-CB2 OMICRON')),
                ('ponovo_pct_200ai', models.IntegerField(verbose_name='PONOVO PCT 200AI')),
                ('factor_hv_hipot_gd6000a', models.IntegerField(verbose_name='FACTOR HV HIPOT GD6000A')),
                ('potencia_tang_delta_avo', models.IntegerField(verbose_name='F.DE POTENCIA Y TANG DELTA AVO')),
                ('micro_contactos_dmo200', models.IntegerField(verbose_name='MICRO R-CONTACTOS DMO200')),
                ('vacuometro_digital', models.IntegerField(verbose_name='VACUOMETRO DIGITAL')),
                ('calidad_energia_metrel', models.IntegerField(verbose_name='CALIDAD DE ENERGIA METREL')),
                ('tiempos_operacion_gdkc_6a', models.IntegerField(verbose_name='TIEMPOS DE OPERACIÓN GDKC-6A')),
                ('tiempos_operacion_egil', models.IntegerField(verbose_name='TIEMPOS DE OPERACIÓN EGIL')),
                ('sata40_tension_minima', models.IntegerField(verbose_name='SATA40 TENSION MINIMA')),
                ('relacion_trans_ttr_gbii', models.IntegerField(verbose_name='RELACION DE TRANS TTR GBII')),
                ('r_devanados_hv_gdzrs_20a', models.IntegerField(verbose_name='R-DEVANADOS HV GDZRS 20A')),
                ('r_devanados_hv_gdzrc_5a', models.IntegerField(verbose_name='R-DEVANADOS HV GDZRC 5A')),
                ('milliohm_sonel', models.IntegerField(verbose_name='MILLIOHM SONEL')),
                ('medidor_mit520_megger', models.IntegerField(verbose_name='MEDIDOR MIT520 MEGGER 5KV')),
                ('medidor_mit500_megger', models.IntegerField(verbose_name='MEDIDOR MIT500 MEGGER 5KV')),
                ('medidor_mic_5010_sonel', models.IntegerField(verbose_name='MEDIDOR MIC 5010 SONEL 5KV')),
                ('medidor_mic_5015_sonel', models.IntegerField(verbose_name='MEDIDOR MIC 5015 SONEL 5KV')),
                ('medidor_mic_5010_sonel_25kv', models.IntegerField(verbose_name='MEDIDOR MIC 5010 SONEL 2,5KV')),
                ('medidor_mic_5005_sonel', models.IntegerField(verbose_name='MEDIDOR MIC 5005 SONEL 2,5KV')),
                ('telurometro_metrotech', models.IntegerField(verbose_name='TELUROMETRO METRONTECH')),
                ('chisporroteo_megger_ots60bp', models.IntegerField(verbose_name='CHISPORROTEO MEGGER OTS60BP')),
                ('circuito_mpc_5_5_50', models.IntegerField(verbose_name='CIRCUITOR MPC-5/5/50')),
                ('vlf_sinus_34kv_megger', models.IntegerField(verbose_name='VLF SINUS 34KV MEGGER')),
                ('probador_cts_cct_xsaid', models.IntegerField(verbose_name='PROBADOR DE CTS CCT - XsaID')),
                ('vaisala_punto_rocio', models.IntegerField(verbose_name='VAISALA PUNTO DE ROCIO')),
                ('recuperador_gas_sf6_gr', models.IntegerField(verbose_name='RECUPERADOR DE GAS SF6 GR')),
                ('recuperador_gas_sf6_pe', models.IntegerField(verbose_name='RECUPERADOR DE GAS SF6 PE')),
                ('bomba_vacio_sf6', models.IntegerField(verbose_name='BOMBA DE VACIO SF6')),
                ('analizador_gas_sf6_grande', models.IntegerField(verbose_name='ANALIZADOR DE GAS SF6 GRANDE')),
                ('analizador_gas_sf6_pequeno', models.IntegerField(verbose_name='ANALIZADOR DE GAS SF6 PEQUEÑO')),
                ('kit_llenado_sf6', models.IntegerField(verbose_name='KIT LLENADO SF6')),
                ('kit_racores', models.IntegerField(verbose_name='KIT DE RACORES')),
                ('pd_scan_descargas_parciales', models.IntegerField(verbose_name='PD SCAN DESCARGAS PARCIALES')),
                ('camara_termografica_nec', models.IntegerField(verbose_name='CAMARA TERMOGRAFICA NEC')),
                ('camara_termografica_irys', models.IntegerField(verbose_name='CAMARA TERMOGRAFICA IRYS')),
                ('fuentes_110_220v', models.IntegerField(verbose_name='FUENTES 110 - 220 V')),
                ('secuencimetro', models.IntegerField(verbose_name='SECUENCIMETRO')),
            ],
        ),
        migrations.CreateModel(
            name='General_dataSE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.CharField(max_length=50)),
                ('Date', models.DateField(default=django.utils.timezone.now)),
                ('Name_project', models.CharField(max_length=50)),
                ('Supervisor', models.CharField(max_length=50)),
                ('Project_code', models.CharField(max_length=50)),
                ('Client', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SafetyEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('botiquin', models.IntegerField(verbose_name='BOTIQUIN')),
                ('camilla', models.IntegerField(verbose_name='CAMILLA')),
                ('colombinas', models.IntegerField(verbose_name='COLOMBINAS')),
                ('conos', models.IntegerField(verbose_name='CONOS')),
                ('candados_seguridad', models.IntegerField(verbose_name='CANDADOS DE SEGURIDAD')),
                ('detector_tension', models.IntegerField(verbose_name='DETECTOR DE TENSION')),
                ('detector_fugas_sf6', models.IntegerField(verbose_name='DETECTOR FUGAS SF6')),
                ('arnes', models.IntegerField(verbose_name='ARNES')),
                ('linea_vida', models.IntegerField(verbose_name='LINEA DE VIDA')),
                ('extintor_multiproposito', models.IntegerField(verbose_name='EXTINTOR MULTIPROPOSITO')),
                ('guantes_dielectricos', models.IntegerField(verbose_name='GUANTES DIELECTRICOS')),
                ('linterna', models.IntegerField(verbose_name='LINTERNA')),
                ('escalera_extension', models.IntegerField(verbose_name='ESCALERA DE EXTENSION')),
                ('escalera_tijera', models.IntegerField(verbose_name='ESCALERA DE TIJERA')),
                ('escalera_2_pasos', models.IntegerField(verbose_name='ESCALERA DE 2 PASOS')),
                ('eslinga_y', models.IntegerField(verbose_name='ESLINGA EN Y')),
                ('eslinga_posicionamiento', models.IntegerField(verbose_name='ESLINGA DE POSICIONAMIENTO')),
            ],
        ),
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
        migrations.CreateModel(
            name='VehicleLogistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehiculo', models.CharField(max_length=100, verbose_name='Vehículo')),
                ('fecha_salida', models.DateField(verbose_name='Fecha Salida')),
                ('fecha_entrada', models.DateField(verbose_name='Fecha Entrada')),
                ('conductor', models.CharField(max_length=100, verbose_name='Conductor(es)')),
                ('ruta', models.CharField(max_length=100, verbose_name='Ruta')),
                ('observaciones', models.TextField(verbose_name='OBSERVACIONES')),
            ],
        ),
    ]
