from django.shortcuts import render, redirect
from .forms import GeneralDataSEForm, EquipmentForm, Tools_and_Accessories_form, SafetyEquipmentForm, VehicleLogisticsForm, SearchForm
from .models import Equipment
from django.http import JsonResponse
from django.db.models import Q
from django.apps import apps
from django.core import serializers
import shutil
from .Cell_assignment import Cell_selectorE, Cell_selectorT, Cell_selectorS
from openpyxl import load_workbook
from PIL import Image
import io
from django.core.files.base import ContentFile
import base64
from openpyxl.drawing.image import Image as OpenpyxlImage
from django.core.files.base import ContentFile
from django.contrib import messages
import os
from django.http import HttpResponse


def Index (request):
    return render(request, 'IndexSE.html')

def searchSE(request, model_name):
    Model = apps.get_model('Solicitud_de_equipos_app', model_name)
    print(f'\n{Model}\n')
    query = request.GET.get('q', '')
    Results = [f.name for f in Model._meta.get_fields() if f.name != 'id' and query in f.name]
        
    return JsonResponse(Results, safe=False )

def GeneralDataSE (request):
    if request.method == 'POST':
        form = GeneralDataSEForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            New_file= f'C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/Solicitud de equipos {data["Date"]}.xlsx'
            
            shutil.copy('C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/Plantilla Solicitud de equipos HTA y otros.xlsx', New_file)
            
            wb = load_workbook(filename=New_file)
            sheet = wb['Hoja1']
            
            sheet['F6'] = data['City'] + ', ' + str(data['Date'])
            sheet['F8'] = data['Name_project']
            sheet['F10'] = data['Supervisor']
            sheet['S6'] = data['Project_code']
            sheet['S8'] = data['Client']
            sheet['S10'] = data['Location']
            
            request.session['New_file'] = New_file
            wb.save(New_file)
            form.save()
            
            return redirect('Equipment')
    else:
        form = GeneralDataSEForm()
        title = 'Datos generales.'
        return render(request, 'General_form.html', {
            'form': form,
            'title': title, 
            })

def Equipment_view (request):
    form = SearchForm(request.GET)
    if  request.method == 'POST':
        if form.is_valid():
            file_name = request.session.get('New_file')
            
            if file_name is None:
                print("No file name in session")
                return redirect('ChoisesFields')
            
            Cell_selectorE(file_name, request.POST)   
            return redirect('ToolsAndAccessories')
    else:
        title = 'Equipos.'
        query = request.GET.get('q', '')
        suggestions = ["cmc_356_omicron", "cmc_353_omicron", "doble_f6150", "ponovo_l336i", "cpc_100_omicron", "cp_td1_omicron", "cp_cu1_omicron", "cp_cr500_omicron", "ct_analyzer_omicron", "franalizer_omicron", "cp_cb2_omicron", "ponovo_pct_200ai", "factor_hv_hipot_gd6000a", "potencia_tang_delta_avo", "micro_contactos_dmo200", "vacuometro_digital", "calidad_energia_metrel", "tiempos_operacion_gdkc_6a", "tiempos_operacion_egil", "sata40_tension_minima", "relacion_trans_ttr_gbii", "r_devanados_hv_gdzrs_20a", "r_devanados_hv_gdzrc_5a", "milliohm_sonel", "medidor_mit520_megger", "medidor_mit500_megger", "medidor_mic_5010_sonel", "medidor_mic_5015_sonel", "medidor_mic_5010_sonel_25kv", "medidor_mic_5005_sonel", "telurometro_metrotech", "chisporroteo_megger_ots60bp", "circuito_mpc_5_5_50", "vlf_sinus_34kv_megger", "probador_cts_cct_xsaid", "vaisala_punto_rocio", "recuperador_gas_sf6_gr", "recuperador_gas_sf6_pe", "bomba_vacio_sf6", "analizador_gas_sf6_grande", "analizador_gas_sf6_pequeno", "kit_llenado_sf6", "kit_racores", "pd_scan_descargas_parciales", "camara_termografica_nec", "camara_termografica_irys", "fuentes_110_220v", "secuencimetro"]
        if query:
            return redirect('search', model_name='Equipment')
        return render(request, 'Forms.html', {
            'model_name': 'Equipment',
            'form': form,
            'title': title,
            'suggestions': suggestions,
            })
    
def ToolsAndAccessories (request):
    form = SearchForm(request.GET)
    if request.method == 'POST':
        if form.is_valid():
            file_name = request.session.get('New_file')
            
            if file_name is None:
                print("No file name in session")
                return redirect('ChoisesFields')
            
            Cell_selectorT(file_name, request.POST) 
            return redirect('SafetyEquipment')
    else:
        suggestions = ["planta_electrica", "juego_de_tierras", "caja_herramientas", "pertiga_escopeta", "pertiga_telescopica", "pistola_calor", "motor_tool", "kit_soldadura_cautin", "pistola_silicona", "sopladora", "taladro", "filtro_sf6", "compresor_pintura", "compresor_aire_seco", "equipo_soldadura", "radio_transmissor", "higrometro", "pata_de_cabra", "ponchadora_hidraulica", "ponchadora_neumatica", "cizalla_manual", "tarrajero", "bomba_para_aceite", "pistola_pintura", "extension_electrica", "esmeril", "sonda", "kit_muestra_aceite", "tarraja", "aspiradora", "pulidora", "caladora", "reflector", "tijera_metal", "poleas", "maleta_sf6", "maquina_filtroprensa"]
        title = 'Herramientas y accesorios.'
        query = request.GET.get('q', '')
        if query:
            return redirect('search', model_name='Tools_and_accessories')
        return render(request, 'Forms.html', {
            'model_name': 'Tools_and_Accessories',
            'form': form,
            'title': title,
            'suggestions': suggestions,
            })
        
def SafetyEquipment_view (request):
    form = SearchForm(request.GET)
    if request.method == 'POST':
        if form.is_valid():
            file_name = request.session.get('New_file')
            
            if file_name is None:
                print("No file name in session")
                return redirect('ChoisesFields')
            
            Cell_selectorS(file_name, request.POST) 
            return redirect('VehicleLogistics')
    else:
        title = 'Equipos de seguridad.'
        suggestions = ["botiquin", "camilla", "colombinas", "conos", "candados_seguridad", "detector_tension", "detector_fugas_sf6", "arnes", "linea_vida", "extintor_multiproposito", "guantes_dielectricos", "linterna", "escalera_extension", "escalera_tijera", "escalera_2_pasos", "eslinga_y", "eslinga_posicionamiento"]
        query = request.GET.get('q', '')
        if query:
            return redirect('search', model_name='Tools_and_accessories')
        return render(request, 'Forms.html', {
            'model_name': 'SafetyEquipment',
            'form': form,
            'title': title,
            'suggestions': suggestions,
            })
        
def VehicleLogistics_view (request):
    if request.method == 'POST':
        
        form = VehicleLogisticsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File_name = request.session.get('New_file')
            
            if File_name is None:
                print("No file name in session")
                # Asegúrate de devolver una respuesta aquí
                return redirect('ChoisesFields')
            
            signature_data = request.POST.get('signature1')
            if ',' in signature_data:
                try:
                    signature_image_data = base64.b64decode(signature_data.split(',')[1])
                    # Procesamiento de la imagen y guardado del archivo...
                    
                    # Asegúrate de devolver una respuesta aquí
                    return redirect('IndexSE')
                except Exception as e:
                    print(f"Error processing signature: {e}")
                    # Devuelve una respuesta de error adecuada aquí
                    return HttpResponse("Error al procesar la firma.", status=500)
            else:
                print("Signature data format is not correct.")
                # Devuelve una respuesta de error adecuada aquí
                return HttpResponse("Formato de datos de firma no es correcto.", status=400)
        else:
            # Si el formulario no es válido, renderiza de nuevo el formulario con los errores
            form = VehicleLogisticsForm()
            title = 'Logistica de vehiculos.'
            return render(request, 'Vehicle_logistics.html', {
                'model_name': 'None',
                'form': form,
                'title': title,
            })
    else:
        # Si el método no es POST, inicializa un formulario vacío
        form = VehicleLogisticsForm()
        return render(request, 'Vehicle_logistics.html', {
            'form': form,
        })

    # Considera agregar un manejo para otros métodos HTTP si es necesario
    return HttpResponse("Método no soportado.", status=405)
        
def Signatures (request):
    return render(request, 'Signatures.html')