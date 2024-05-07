from django .shortcuts import render, redirect
from django.core.files.storage import default_storage
from .froms import DatosGeneralesForm, InspeccionForm, FrontPartForm, SideForm, BackPartForm
from .models import Datos_generales, Inspeccion, Vehiculo, Histoial_archivos, Images
from builtins import ValueError
from openpyxl import Workbook, load_workbook
from django.http import HttpResponse
from datetime import datetime
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from django.http import JsonResponse
import shutil
from django.utils import timezone
import os
import pandas as pd
import string
import time
from docx import Document
from docx.shared import Inches
import io
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
from .Conversor import convert_word_to_pdf



hoy = datetime.now()

dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
dia_semana = dias_semana[hoy.weekday()]
date_str = datetime.now().strftime('%Y-%m-%d')
hora = hoy.hour
hoy_y_hora = datetime.now().strftime('%Y/%m/%d Hora %H:%M')


def Search(request):
    q = request.GET.get('q', '')
    vehiculos = Vehiculo.objects.filter(Placa__icontains=q)
    results = [vehiculo.Placa for vehiculo in vehiculos]
    return JsonResponse(results, safe=False)

def index(request):
    return render(request, 'Index.html')

def FormG (request):
    if request.method == 'POST':
        print (request.POST)
        
        form = DatosGeneralesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            General_Data = form.cleaned_data
            print (General_Data)
            
            vehiculo = General_Data['vehiculo']
            
            
            historial_archivos = Histoial_archivos.objects.filter(vehiculo=General_Data['vehiculo'])
            if historial_archivos.exists():
                ultimo_archivo = historial_archivos.latest('created_at')
                nombre_archivo = ultimo_archivo.Nombre_archivo
                word_file_name = f'C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/{str(General_Data["vehiculo"])}/Archivos de imagenes/Imagenes.docx'
                
                
                now = timezone.now()
                days_passed = (now - ultimo_archivo.created_at).days
                   
                                       
                if days_passed == 29:
                    Mes_pasado = now - timezone.timedelta(days=30)
                    convert_word_to_pdf(f"C:\\Users\\Dagelec LTDA\\Desktop\\Pruebas_excel\\{str(General_Data['vehiculo'])}\\Archivos de imagenes\\Imagenes.docx", f"C:\\Users\\Dagelec LTDA\\Desktop\\Pruebas_excel\\{str(General_Data['vehiculo'])}\\Archivos de imagenes\\Imagenes del mes {Mes_pasado}.pdf")
                    
                    doc = Document()
                    
                    new_file_name = f"C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/{str(General_Data['vehiculo'])}/{str(General_Data['vehiculo'])}_{date_str}.xlsx"
                    shutil.copy('C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/Plantilla.xlsx', new_file_name)
                    Historial = Histoial_archivos.objects.create(vehiculo = General_Data['vehiculo'], Nombre_archivo = new_file_name)
                    Historial.save()
                    wb = load_workbook(filename= new_file_name)
                    request.session['nombre_archivo'] = new_file_name
                    
                    if days_passed >= 20:
                        Semana = "Semana 4"
                        request.session['Sheet'] = Semana
                    elif days_passed >= 13: 
                        Semana = "Semana 3"
                        request.session['Sheet'] = Semana
                    elif days_passed >= 6:
                        Semana = "Semana 2"
                        request.session['Sheet'] = Semana
                    else:
                        Semana = "Semana 1"
                        request.session['Sheet'] = Semana
               
                doc = Document(word_file_name)
                wb = load_workbook(filename= nombre_archivo)
                request.session['word_file_name'] = word_file_name
                request.session['Ruta'] = str(General_Data['vehiculo'])
                request.session['nombre_archivo'] = nombre_archivo
                
                doc.add_heading(str(hoy_y_hora), 0)
                   
            else:  
                folder_path = f"C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/{str(General_Data['vehiculo'])}"
                folder_path2 = f"C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/{str(General_Data['vehiculo'])}/Archivos de imagenes"
                os.makedirs(folder_path2, exist_ok=True)
                os.makedirs(folder_path, exist_ok=True)
                
                word_file_name = f'C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/{str(General_Data["vehiculo"])}/Archivos de imagenes/Imagenes.docx'
                new_file_name = f"C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/{str(General_Data['vehiculo'])}/{str(General_Data['vehiculo'])}_{date_str}.xlsx"
                shutil.copy('C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/Plantilla.xlsx', new_file_name)
                doc = Document()
                
                doc.add_heading(str(hoy_y_hora), 0)
                
                Historial = Histoial_archivos.objects.create(vehiculo = General_Data['vehiculo'], Nombre_archivo = new_file_name)
                Historial.save()
                
                wb = load_workbook(filename= new_file_name)
                request.session['word_file_name'] = word_file_name
                request.session['nombre_archivo'] = new_file_name
                Semana = 'Semana 1'
                request.session['Sheet'] = Semana
                
            sheet = wb[Semana]
            
            sheet['F5'] = vehiculo.Marca
            sheet["F7"] = vehiculo.Numero_tarjeta_de_propiedad
            sheet["F8"] = vehiculo.Fecha_emicion_de_revision_tecnomecanica
            sheet["L5"] = vehiculo.Modelo
            sheet["L7"] = vehiculo.Fecha_emicion_SOAT
            sheet["L8"] = vehiculo.Fecha_emicion_poliza
            
            sheet['F6'] = str(General_Data['vehiculo'])
            sheet['L6'] = General_Data['Proyecto']
            if dia_semana == 'Lunes':
                if hora >= 6 and hora < 14:
                    sheet['G42'] = General_Data['Nombre']
                elif hora >= 14 and hora < 22:
                    sheet['G43'] = General_Data['Nombre'] 
                else:
                    sheet['G44'] = General_Data['Nombre']      
                sheet['G45'] = General_Data['Fecha']
            elif dia_semana == 'Martes':
                if hora >= 6 and hora < 14:
                    sheet['H42'] = General_Data['Nombre']
                elif hora >= 14 and hora < 22:
                    sheet['H43'] = General_Data['Nombre'] 
                else:
                    sheet['H44'] = General_Data['Nombre']   
                sheet['H45'] = General_Data['Fecha']
            elif dia_semana == 'Miércoles':
                if hora >= 6 and hora < 14:
                    sheet['I42'] = General_Data['Nombre']
                elif hora >= 14 and hora < 22:
                    sheet['I43'] = General_Data['Nombre'] 
                else:
                    sheet['I44'] = General_Data['Nombre']   
                sheet['I45'] = General_Data['Fecha']
            elif dia_semana == 'Jueves':
                if hora >= 6 and hora < 14:
                    sheet['J42'] = General_Data['Nombre']
                elif hora >= 14 and hora < 22:
                    sheet['J43'] = General_Data['Nombre'] 
                else:
                    sheet['J44'] = General_Data['Nombre']   
                sheet['J45'] = General_Data['Fecha']
            elif dia_semana == 'Viernes':
                if hora >= 6 and hora < 14:
                    sheet['K42'] = General_Data['Nombre']
                elif hora >= 14 and hora < 22:
                    sheet['K43'] = General_Data['Nombre'] 
                else:
                    sheet['K44'] = General_Data['Nombre']   
                sheet['K45'] = General_Data['Fecha']
            elif dia_semana == 'Sábado':
                if hora >= 6 and hora < 14:
                    sheet['L42'] = General_Data['Nombre']
                elif hora >= 14 and hora < 22:
                    sheet['L43'] = General_Data['Nombre'] 
                else:
                    sheet['L44'] = General_Data['Nombre']   
                sheet['L45'] = General_Data['Fecha']
            else:
                if hora >= 6 and hora < 14:
                    sheet['M342'] = General_Data['Nombre']
                elif hora >= 14 and hora < 22:
                    sheet['M43'] = General_Data['Nombre'] 
                else:
                    sheet['M44'] = General_Data['Nombre']   
                sheet['M45'] = General_Data['Fecha']
            
            doc.save(word_file_name)
            wb.save(filename= request.session.get('nombre_archivo'))
            return redirect('FormI')
        else:
            if 'vehiculo' in form.errors:
                Error = 'El vehículo con placa {} no existe.'.format(form.data['vehiculo'])
                print(form.errors['vehiculo'])
            return render(request, 'Forms/FormG.html', {'form': form,
                                                        'Error': Error
                                                        })
    else:
        form = DatosGeneralesForm() 
        return render(request, 'Forms/FormG.html', {'form': form})

def FormI(request):
    if request.method == 'POST':
        global dia_semana
        form = InspeccionForm(request.POST, request.FILES)
        
        images=Images.objects.create(
            Nivel_aceite_NC = request.FILES['Nivel_aceite_NC'] if 'Nivel_aceite_NC' in request.FILES else None,
            capot_asegurado_NC = request.FILES['capot_asegurado_NC'] if 'capot_asegurado_NC' in request.FILES else None,
            bornes_baterias_ajustados_NC = request.FILES['bornes_baterias_ajustados_NC'] if 'bornes_baterias_ajustados_NC' in request.FILES else None,
            indicadores_tablero_control_NC = request.FILES['indicadores_tablero_control_NC'] if 'indicadores_tablero_control_NC' in request.FILES else None,
            aire_acondicionado_NC = request.FILES['aire_acondicionado_NC'] if 'aire_acondicionado_NC' in request.FILES else None,
            freno_estacionamiento_NC = request.FILES['freno_estacionamiento_NC'] if 'freno_estacionamiento_NC' in request.FILES else None,
            limpiaparabrisas_NC = request.FILES['limpiaparabrisas_NC'] if 'limpiaparabrisas_NC' in request.FILES else None,
            pito_electrico_NC = request.FILES['pito_electrico_NC'] if 'pito_electrico_NC' in request.FILES else None,
            cinturones_seguridad_NC = request.FILES['cinturones_seguridad_NC'] if 'cinturones_seguridad_NC' in request.FILES else None,
            equipo_prevencion_seguridad_NC = request.FILES['equipo_prevencion_seguridad_NC'] if 'equipo_prevencion_seguridad_NC' in request.FILES else None,
            botiquin_primeros_auxilios_NC = request.FILES['botiquin_primeros_auxilios_NC'] if 'botiquin_primeros_auxilios_NC' in request.FILES else None,
            extintor_NC = request.FILES['extintor_NC'] if 'extintor_NC' in request.FILES else None,
            kit_carreteras_NC = request.FILES['kit_carreteras_NC'] if 'kit_carreteras_NC' in request.FILES else None,
            sensor_externo_velocidad_NC = request.FILES['sensor_externo_velocidad_NC'] if 'sensor_externo_velocidad_NC' in request.FILES else None, 
        )
        
        if form.is_valid():
            Sheet = request.session.get('Sheet', None)
            Word = request.session.get('word_file_name', None)
            if Sheet is None:
                return redirect('FormG')
            elif Word is None:
                print ('¡¡¡Eror el archivo word no existe!!!')
                return redirect('FormG')
            
            nombre_archivo = request.session.get('nombre_archivo')
            inspeccion = form.cleaned_data
            wb = load_workbook(filename= nombre_archivo)
            sheet = wb[Sheet]
            
            
            N=12
            
            if dia_semana == 'Lunes':
                
                for field, value in form.cleaned_data.items():
                   
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else: 
                            sheet['G'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['G'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['G'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:  
                            sheet['G'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['G'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['G'+str(N)] = value
                            N+=1
            
            elif dia_semana == 'Martes':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['H'+str(N)] = value.name
                        else: 
                            sheet['H'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['H'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['H'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['H'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['H'+str(N)] = value.name
                        else:  
                            sheet['H'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['H'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['H'+str(N)] = value
                            N+=1    
        
            elif dia_semana == 'Miércoles':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['I'+str(N)] = value.name
                        else: 
                            sheet['I'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['I'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['I'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['I'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['I'+str(N)] = value.name
                        else:  
                            sheet['I'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['I'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['I'+str(N)] = value
                            N+=1
                            
            elif dia_semana == 'Jueves':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else: 
                            sheet['J'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['J'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['J'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:  
                            sheet['J'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['J'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['J'+str(N)] = value
                            N+=1
                            
            elif dia_semana == 'Viernes':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        else: 
                            sheet['K'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['K'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['K'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        else:  
                            sheet['K'+str(N)] = value   
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        else:
                            sheet['K'+str(N)] = value
                            
            elif dia_semana == 'Sábado':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['L'+str(N)] = value.name
                        else: 
                            sheet['L'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['L'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['L'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['L'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['L'+str(N)] = value.name
                        else:  
                            sheet['L'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['L'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['L'+str(N)] = value
                            N+=1
                            
            elif dia_semana == 'Domingo':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else: 
                            sheet['M'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['M'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['M'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:  
                            sheet['M'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['M'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['M'+str(N)] = value
                            N+=1

            wb_C = None
            try:
                wb_C = load_workbook('C:/Users/Dagelec LTDA//Desktop/Pruebas_excel/Vehículo LTS-285/Copy.xlsx') 
            except FileNotFoundError:
                pass

            if wb_C is not None:
                Sheet_O = wb[Sheet]
                Sheet_C = wb_C[Sheet]

                rows_O = Sheet_O['B12':'M27']  
                rows_C = Sheet_C['B12':'M27']

                df_O = pd.DataFrame([[cell.value for cell in row] for row in rows_O])
                df_C = pd.DataFrame([[cell.value for cell in row] for row in rows_C])

                differences = df_C.compare(df_O)
                differences = differences.dropna(how='all')
                N = 49


                for index, row in differences.iterrows():
                    for column in differences.columns:
                        if column[1] == 'self' and pd.notna(row[column]):
                            previous_value = row[(column[0], "self")]
                            new_value = row[(column[0], "other")]

                            if previous_value != 'none':
                                message = (f'En el campo {df_O.loc[index, 0]} fue cambiado de {previous_value} a {new_value}.')
                            else:
                                dia_semana = ''

                            if dia_semana == 'Lunes':
                                sheet['A'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Martes':
                                sheet['C'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Miercoles':
                                sheet['E'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Jueves':
                                sheet['G'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Viernes':
                                sheet['I'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Sábado':
                                sheet['K'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Domingo':
                                sheet['M'+str(N)] = message
                                N = N + 1
                            else:
                                dia_semana = dias_semana[hoy.weekday()]
                                pass
            
            doc = Document(Word)
            
            for file_name, file in request.FILES.items():
                    
                    paragraph = doc.add_paragraph()
                    run = paragraph.add_run(file_name)
                    run.font.size = Pt(16)
                    doc.add_picture(file, width=Inches(3))
                    paragraph = doc.add_paragraph()
                    run = paragraph.add_run(file.name)
                    run.font.size = Pt(12)

            
            request.session['N'] = N
            wb.save(nombre_archivo)
            doc.save(Word) 
            images.save()                
            form.save()
            return redirect ('FormFP')
        else:
            Titulo = 'Formulario de Inspección.'
            error = 'Tienes que llenar todos los campos para continuar con el formulario.'
            form = InspeccionForm()
            return render(request, 'Forms/Form.html', {'form': form,
                                                              'error': error,
                                                              'Title' : Titulo
                                                              })
                
    else:
        Titulo = 'Formulario de Inspección.'
        form = InspeccionForm()
        return render(request, 'Forms/Form.html', {'form': form,
                                                          'Title' : Titulo
                                                          })

def FormFP(request):
    if request.method == 'POST':

        form = FrontPartForm(request.POST, request.FILES)
        
        images=Images.objects.create(
            funcionamiento_luces_delanteras_NC = request.FILES['funcionamiento_luces_delanteras_NC'] if 'funcionamiento_luces_delanteras_NC' in request.FILES else None,
            vidrio_delantero_sin_fisuras_NC = request.FILES['vidrio_delantero_sin_fisuras_NC'] if 'vidrio_delantero_sin_fisuras_NC' in request.FILES else None,
            placa_delantera_legible_NC = request.FILES['placa_delantera_legible_NC'] if 'placa_delantera_legible_NC' in request.FILES else None,
            Labrado_de_las_llantas_delanteras_NC = request.FILES['Labrado_de_las_llantas_delanteras_NC'] if 'Labrado_de_las_llantas_delanteras_NC' in request.FILES else None,
        )
        
        if form.is_valid():
            global dia_semana
            Sheet = request.session.get('Sheet', None)
            N2 = request.session.get('N', None)
            Word = request.session.get('word_file_name', None)
            
            if Sheet is None:
                return redirect('FormG')
            nombre_archivo = request.session.get('nombre_archivo')
            inspeccion = form.cleaned_data
            print(inspeccion)
            wb = load_workbook(filename= nombre_archivo)
            sheet = wb[Sheet]
            N=28
            
            if dia_semana == 'Lunes':
                
                for field, value in form.cleaned_data.items():
                   
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else: 
                            sheet['G'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['G'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['G'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:  
                            sheet['G'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['G'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['G'+str(N)] = value
                            N+=1
            
            elif dia_semana == 'Martes':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['H'+str(N)] = value.name
                        else: 
                            sheet['H'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['H'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['H'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['H'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['H'+str(N)] = value.name
                        else:  
                            sheet['H'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['H'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['H'+str(N)] = value
                            N+=1    
        
            elif dia_semana == 'Miércoles':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['I'+str(N)] = value.name
                        else: 
                            sheet['I'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['I'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['I'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['I'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['I'+str(N)] = value.name
                        else:  
                            sheet['I'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['I'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['I'+str(N)] = value
                            N+=1
                            
            elif dia_semana == 'Jueves':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else: 
                            sheet['J'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['J'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['J'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:  
                            sheet['J'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['J'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['J'+str(N)] = value
                            N+=1
                            
            elif dia_semana == 'Viernes':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        else: 
                            sheet['K'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['K'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['K'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        else:  
                            sheet['K'+str(N)] = value   
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        else:
                            sheet['K'+str(N)] = value
                            
            elif dia_semana == 'Sábado':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['L'+str(N)] = value.name
                        else: 
                            sheet['L'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['L'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['L'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['L'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['L'+str(N)] = value.name
                        else:  
                            sheet['L'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['L'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['L'+str(N)] = value
                            N+=1
                            
            elif dia_semana == 'Domingo':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else: 
                            sheet['M'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['M'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['M'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:  
                            sheet['M'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['M'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['M'+str(N)] = value
                            N+=1

            wb_C = None
            try:
                wb_C = load_workbook('C:/Users/Dagelec LTDA//Desktop/Pruebas_excel/Vehículo LTS-285/Copy.xlsx') 
            except FileNotFoundError:
                pass

            if wb_C is not None:
                Sheet_O = wb[Sheet]
                Sheet_C = wb_C[Sheet]

                rows_O = Sheet_O['C28':'M31']  
                rows_C = Sheet_C['C28':'M31']

                df_O = pd.DataFrame([[cell.value for cell in row] for row in rows_O])
                df_C = pd.DataFrame([[cell.value for cell in row] for row in rows_C])

                differences = df_C.compare(df_O)
                differences = differences.dropna(how='all')
                N = 46


                for index, row in differences.iterrows():
                    for column in differences.columns:
                        if column[1] == 'self' and pd.notna(row[column]):
                            previous_value = row[(column[0], "self")]
                            new_value = row[(column[0], "other")]

                            if previous_value != 'none':
                                message = (f'En el campo {df_O.loc[index, 0]} fue cambiado de {previous_value} a {new_value}.')
                            else:
                                dia_semana = ''

                            if dia_semana == 'Lunes':
                                sheet['A'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Martes':
                                sheet['C'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Miercoles':
                                sheet['E'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Jueves':
                                sheet['G'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Viernes':
                                sheet['I'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Sábado':
                                sheet['K'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Domingo':
                                sheet['M'+str(N)] = message
                                N = N + 1
                            else:
                                dia_semana = dias_semana[hoy.weekday()]
                                pass

            doc = Document(Word)
            
            for file_name, file in request.FILES.items():
                    
                    paragraph = doc.add_paragraph()
                    run = paragraph.add_run(file_name)
                    run.font.size = Pt(16)
                    doc.add_picture(file, width=Inches(3))
                    paragraph = doc.add_paragraph()
                    run = paragraph.add_run(file.name)
                    run.font.size = Pt(12)
            
            wb.save(nombre_archivo)                   
            images.save()
            doc.save(Word)
            form.save()
            return redirect ('FormS')
        else:
            Titulo = 'Formulario de Inspección de la parte delantera.'
            error = 'Tienes que llenar todos los campos para continuar con el formulario.'
            form = FrontPartForm(request.POST, request.FILES)
            return render(request, 'Forms/Formpruebas.html', {'form': form, 
                                                              'error': error, 
                                                              'Title': Titulo
                                                              })
                
    else:
        Titulo = 'Formulario de Inspección de la parte delantera.'
        form = FrontPartForm()
        return render(request, 'Forms/Form.html', {'form': form,
                                                          'Title': Titulo
                                                          })

def FormS (request):
    if request.method == 'POST':
        form = SideForm(request.POST, request.FILES)
        
        images=Images.objects.create(
            carroceria_buen_estado_NC = request.FILES['carroceria_buen_estado_NC'] if 'carroceria_buen_estado_NC' in request.FILES else None,
            vidrios_laterales_sin_fisuras_NC = request.FILES['vidrios_laterales_sin_fisuras_NC'] if 'vidrios_laterales_sin_fisuras_NC' in request.FILES else None,
            direccionales_funcionando_NC = request.FILES['direccionales_funcionando_NC'] if 'direccionales_funcionando_NC' in request.FILES else None,
            espejo_exterior_buen_estado_NC = request.FILES['espejo_exterior_buen_estado_NC'] if 'espejo_exterior_buen_estado_NC' in request.FILES else None,
             sin_fugas_tanque_combustible = request.FILES['sin_fugas_tanque_combustible'] if 'sin_fugas_tanque_combustible' in request.FILES else None,
        )
        
        if form.is_valid():
            global dia_semana
            Sheet = request.session.get('Sheet', None)
            Word = request.session.get('word_file_name', None)
            
            N2 = request.session.get('N', None)
            if Sheet is None:
                return redirect('FormG')
            nombre_archivo = request.session.get('nombre_archivo')
            inspeccion = form.cleaned_data
            print(inspeccion)
            wb = load_workbook(filename= nombre_archivo)
            sheet = wb[Sheet]
            N=32
            
            if dia_semana == 'Lunes':
                
                for field, value in form.cleaned_data.items():
                   
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else: 
                            sheet['G'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['G'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['G'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:  
                            sheet['G'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['G'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['G'+str(N)] = value
                            N+=1
            
            elif dia_semana == 'Martes':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['H'+str(N)] = value.name
                        else: 
                            sheet['H'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['H'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['H'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['H'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['H'+str(N)] = value.name
                        else:  
                            sheet['H'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['H'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['H'+str(N)] = value
                            N+=1    
        
            elif dia_semana == 'Miércoles':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['I'+str(N)] = value.name
                        else: 
                            sheet['I'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['I'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['I'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['I'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['I'+str(N)] = value.name
                        else:  
                            sheet['I'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['I'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['I'+str(N)] = value
                            N+=1
                            
            elif dia_semana == 'Jueves':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else: 
                            sheet['J'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['J'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['J'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:  
                            sheet['J'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['J'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['J'+str(N)] = value
                            N+=1
                            
            elif dia_semana == 'Viernes':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        else: 
                            sheet['K'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['K'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['K'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        else:  
                            sheet['K'+str(N)] = value   
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        else:
                            sheet['K'+str(N)] = value
                            
            elif dia_semana == 'Sábado':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['L'+str(N)] = value.name
                        else: 
                            sheet['L'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['L'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['L'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['L'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['L'+str(N)] = value.name
                        else:  
                            sheet['L'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['L'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['L'+str(N)] = value
                            N+=1
                            
            elif dia_semana == 'Domingo':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else: 
                            sheet['M'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['M'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['M'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:  
                            sheet['M'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['M'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['M'+str(N)] = value
                            N+=1

            wb_C = None
            try:
                wb_C = load_workbook('C:/Users/Dagelec LTDA//Desktop/Pruebas_excel/Vehículo LTS-285/Copy.xlsx') 
            except FileNotFoundError:
                pass

            if wb_C is not None:
                Sheet_O = wb[Sheet]
                Sheet_C = wb_C[Sheet]

                rows_O = Sheet_O['C32':'M36']  
                rows_C = Sheet_C['C37':'M41']

                df_O = pd.DataFrame([[cell.value for cell in row] for row in rows_O])
                df_C = pd.DataFrame([[cell.value for cell in row] for row in rows_C])

                differences = df_C.compare(df_O)
                differences = differences.dropna(how='all')
                N = 46


                for index, row in differences.iterrows():
                    for column in differences.columns:
                        if column[1] == 'self' and pd.notna(row[column]):
                            previous_value = row[(column[0], "self")]
                            new_value = row[(column[0], "other")]

                            if previous_value != 'none':
                                message = (f'En el campo {df_O.loc[index, 0]} fue cambiado de {previous_value} a {new_value}.')
                            else:
                                dia_semana = ''

                            if dia_semana == 'Lunes':
                                sheet['A'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Martes':
                                sheet['C'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Miercoles':
                                sheet['E'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Jueves':
                                sheet['G'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Viernes':
                                sheet['I'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Sábado':
                                sheet['K'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Domingo':
                                sheet['M'+str(N)] = message
                                N = N + 1
                            else:
                                dia_semana = dias_semana[hoy.weekday()]
                                pass
            
            doc = Document(Word)
            
            for file_name, file in request.FILES.items():
                    
                    paragraph = doc.add_paragraph()
                    run = paragraph.add_run(file_name)
                    run.font.size = Pt(16)
                    doc.add_picture(file, width=Inches(3))
                    paragraph = doc.add_paragraph()
                    run = paragraph.add_run(file.name)
                    run.font.size = Pt(12)
            
            
            wb.save(nombre_archivo)                   
            images.save()
            doc.save(Word)
            form.save()
            return redirect ('FormBP')
        else:
            Titulo = 'Formulario de inspección de la parte del costado.'
            error = 'Tienes que llenar todos los campos para continuar con el formulario.'
            form = SideForm(request.POST, request.FILES)
            return render(request, 'Forms/Form.html', {'form': form, 
                                                              'error': error, 
                                                              'Title': Titulo
                                                              })
                
    else:
        Titulo = 'Formulario de inspección de la parte del costado.'
        form = SideForm()
        return render(request, 'Forms/Form.html', {'form': form,
                                                          'Title': Titulo
                                                          })
        
def FormBP(request):
    if request.method == 'POST':
        form = BackPartForm(request.POST, request.FILES)
        
        images=Images.objects.create(
            luces_traseras_funcionando_NC = request.FILES['luces_traseras_funcionando_NC'] if 'luces_traseras_funcionando_NC' in request.FILES else None,
            sonido_alarma_reversa_NC = request.FILES['sonido_alarma_reversa_NC'] if 'sonido_alarma_reversa_NC' in request.FILES else None,
            labrado_llantas_traseras_NC = request.FILES['labrado_llantas_traseras_NC'] if 'labrado_llantas_traseras_NC' in request.FILES else None,
            labrado_llanta_repuesto_NC = request.FILES['labrado_llanta_repuesto_NC'] if 'labrado_llanta_repuesto_NC' in request.FILES else None,
            placa_trasera_legible_NC = request.FILES['placa_trasera_legible_NC'] if 'placa_trasera_legible_NC' in request.FILES else None,
        )
        
        if form.is_valid():
            global dia_semana
            Sheet = request.session.get('Sheet', None)
            N2 = request.session.get('N', None)
            if Sheet is None:
                return redirect('FormG')
            Ruta = request.session.get('Ruta')
            nombre_archivo = request.session.get('nombre_archivo')
            Word = request.session.get('word_file_name', None)
            
            inspeccion = form.cleaned_data
            file_path = f'C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/{Ruta}/Copy.xlsx'
            print(inspeccion)
            wb = load_workbook(filename= nombre_archivo)
            sheet = wb[Sheet]
            N=37
            
            if dia_semana == 'Lunes':
                
                for field, value in form.cleaned_data.items():
                   
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else: 
                            sheet['G'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['G'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['G'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:  
                            sheet['G'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['G'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['G'+str(N)] = value
                            N+=1
            
            elif dia_semana == 'Martes':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['H'+str(N)] = value.name
                        else: 
                            sheet['H'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['H'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['H'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['H'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['H'+str(N)] = value.name
                        else:  
                            sheet['H'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['H'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['H'+str(N)] = value
                            N+=1    
        
            elif dia_semana == 'Miércoles':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['I'+str(N)] = value.name
                        else: 
                            sheet['I'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['I'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['I'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['I'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['I'+str(N)] = value.name
                        else:  
                            sheet['I'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['I'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['I'+str(N)] = value
                            N+=1
                            
            elif dia_semana == 'Jueves':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else: 
                            sheet['J'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['J'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['J'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:  
                            sheet['J'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['J'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['J'+str(N)] = value
                            N+=1
                            
            elif dia_semana == 'Viernes':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        else: 
                            sheet['K'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['K'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['K'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        else:  
                            sheet['K'+str(N)] = value   
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['K'+str(N)] = value.name
                        else:
                            sheet['K'+str(N)] = value
                            
            elif dia_semana == 'Sábado':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['L'+str(N)] = value.name
                        else: 
                            sheet['L'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['L'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['L'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['L'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['L'+str(N)] = value.name
                        else:  
                            sheet['L'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['L'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['L'+str(N)] = value
                            N+=1
                            
            elif dia_semana == 'Domingo':
                
                for field, value in form.cleaned_data.items():
                    
                    if isinstance(value, InMemoryUploadedFile):
                        file_content = value.read()
                    elif value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else: 
                            sheet['M'+str(N)] = value
                            N+=1
                            
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        elif hasattr(value, 'temporary_file_path'):
                            sheet['M'+str(N)] = value.temporary_file_path()
                        else:
                            sheet['M'+str(N)] = value
                            N+=1
                            
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:  
                            sheet['M'+str(N)] = value
                            N+=1
                            
                    else:
                        if isinstance(value, TemporaryUploadedFile):
                            sheet['M'+str(N)] = value.temporary_file_path() 
                        else:
                            sheet['M'+str(N)] = value
                            N+=1

            wb_C = None
            try:
                wb_C = load_workbook('C:/Users/Dagelec LTDA//Desktop/Pruebas_excel/Vehículo LTS-285/Copy.xlsx') 
            except FileNotFoundError:
                pass

            if wb_C is not None:
                Sheet_O = wb[Sheet]
                Sheet_C = wb_C[Sheet]

                rows_O = Sheet_O['C37':'M41']  
                rows_C = Sheet_C['C37':'M41']

                df_O = pd.DataFrame([[cell.value for cell in row] for row in rows_O])
                df_C = pd.DataFrame([[cell.value for cell in row] for row in rows_C])

                differences = df_C.compare(df_O)
                differences = differences.dropna(how='all')
                N = 46


                for index, row in differences.iterrows():
                    for column in differences.columns:
                        if column[1] == 'self' and pd.notna(row[column]):
                            previous_value = row[(column[0], "self")]
                            new_value = row[(column[0], "other")]

                            if previous_value != 'none':
                                message = (f'En el campo {df_O.loc[index, 0]} fue cambiado de {previous_value} a {new_value}.')
                            else:
                                dia_semana = ''

                            if dia_semana == 'Lunes':
                                sheet['A'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Martes':
                                sheet['C'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Miercoles':
                                sheet['E'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Jueves':
                                sheet['G'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Viernes':
                                sheet['I'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Sábado':
                                sheet['K'+str(N)] = message
                                N = N + 1
                            elif dia_semana == 'Domingo':
                                sheet['M'+str(N)] = message
                                N = N + 1
                            else:
                                dia_semana = dias_semana[hoy.weekday()]
                                pass 
            
            doc = Document(Word)
    
            
            for file_name, file in request.FILES.items():
                    
                    paragraph = doc.add_paragraph()
                    run = paragraph.add_run(file_name)
                    run.font.size = Pt(16)
                    doc.add_picture(file, width=Inches(3))
                    paragraph = doc.add_paragraph()
                    run = paragraph.add_run(file.name)
                    run.font.size = Pt(12)
            
            os.remove(file_path)
            wb.save(nombre_archivo)                      
            form.save()
            doc.save(Word)
            images.save()
            return redirect ('Index')
        else:
            Titulo = 'Formulario de Inspección de la parte trasera.'
            error = 'Tienes que llenar todos los campos para continuar con el formulario.'
            form = BackPartForm(request.POST, request.FILES)
            return render(request, 'Forms/Form.html', {'form': form, 
                                                              'error': error, 
                                                              'Title': Titulo
                                                              })
                
    else:
        Titulo = 'Formulario de Inspección de la parte trasera.'
        form = BackPartForm()
        return render(request, 'Forms/Form.html', {'form': form,
                                                          'Title': Titulo
                                                          })