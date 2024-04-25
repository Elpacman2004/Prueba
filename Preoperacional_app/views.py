from django .shortcuts import render, redirect
from .froms import DatosGeneralesForm, InspeccionForm, FrontPartForm, SideForm, BackPartForm
from .models import Datos_generales, Inspeccion, Vehiculo, Histoial_archivos
from builtins import ValueError
from openpyxl import Workbook, load_workbook
from django.http import HttpResponse
from datetime import datetime
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
import shutil
from django.utils import timezone
import os
import pandas as pd
import string


hoy = datetime.now()

dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
dia_semana = dias_semana[hoy.weekday()]
date_str = datetime.now().strftime('%Y-%m-%d')
hora = hoy.hour


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
            
            historial_archivos = Histoial_archivos.objects.filter(vehiculo=General_Data['vehiculo'])
            if historial_archivos.exists():
                ultimo_archivo = historial_archivos.latest('created_at')
                nombre_archivo = ultimo_archivo.Nombre_archivo
                
                shutil.copy(nombre_archivo, f"C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/{str(General_Data['vehiculo'])}/Copy.xlsx")
                
                now = timezone.now()
                days_passed = (now - ultimo_archivo.created_at).days
                
                wb = load_workbook(filename= nombre_archivo)
                request.session['Ruta'] = str(General_Data['vehiculo'])
                request.session['nombre_archivo'] = nombre_archivo
                if days_passed == 7 or 14 or 21:
                    wb = load_workbook(filename= nombre_archivo)
                    if days_passed ==7:
                        ws = wb.create_sheet("Semana 2")
                    elif days_passed == 14:
                        ws = wb.create_sheet("Semana 3")
                    elif days_passed == 21:
                        ws = wb.create_sheet("Semana 4")
                        
                elif days_passed == 30:
                    new_file_name = f"C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/{str(General_Data['vehiculo'])}/{str(General_Data['vehiculo'])}_{date_str}.xlsx"
                    shutil.copy('C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/Plantilla.xlsx', new_file_name)
                    Historial = Histoial_archivos.objects.create(vehiculo = General_Data['vehiculo'], Nombre_archivo = new_file_name)
                    Historial.save()
                    wb = load_workbook(filename= new_file_name)
                    request.session['nombre_archivo'] = new_file_name
                    
            else:
                folder_path = f"C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/{str(General_Data['vehiculo'])}"
                os.makedirs(folder_path, exist_ok=True)
                new_file_name = f"C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/{str(General_Data['vehiculo'])}/{str(General_Data['vehiculo'])}_{date_str}.xlsx"
                shutil.copy('C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/Plantilla.xlsx', new_file_name)
                Historial = Histoial_archivos.objects.create(vehiculo = General_Data['vehiculo'], Nombre_archivo = new_file_name)
                Historial.save()
                wb = load_workbook(filename= new_file_name)
                request.session['nombre_archivo'] = new_file_name
                
            if days_passed >= 21:
                Semana = "Semana 4"
                request.session['Sheet'] = Semana
            elif days_passed >= 14: 
                Semana = "Semana 3"
                request.session['Sheet'] = Semana
            elif days_passed >= 7:
                Semana = "Semana 2"
                request.session['Sheet'] = Semana
            else:
                Semana = "Semana 1"
                request.session['Sheet'] = Semana
                
            sheet = wb[Semana]
            sheet['E5'] = str(General_Data['vehiculo'])
            sheet['U5'] = General_Data['Proyecto']
            if dia_semana == 'Lunes':
                if hora >= 6 and hora < 14:
                    sheet['G39'] = General_Data['Nombre']
                elif hora >= 14 and hora < 22:
                    sheet['G40'] = General_Data['Nombre'] 
                else:
                    sheet['G41'] = General_Data['Nombre']      
                sheet['G42'] = General_Data['Fecha']
            elif dia_semana == 'Martes':
                if hora >= 6 and hora < 14:
                    sheet['J39'] = General_Data['Nombre']
                elif hora >= 14 and hora < 22:
                    sheet['J40'] = General_Data['Nombre'] 
                else:
                    sheet['J41'] = General_Data['Nombre']   
                sheet['J42'] = General_Data['Fecha']
            elif dia_semana == 'Miércoles':
                if hora >= 6 and hora < 14:
                    sheet['M39'] = General_Data['Nombre']
                elif hora >= 14 and hora < 22:
                    sheet['M40'] = General_Data['Nombre'] 
                else:
                    sheet['M41'] = General_Data['Nombre']   
                sheet['M42'] = General_Data['Fecha']
            elif dia_semana == 'Jueves':
                if hora >= 6 and hora < 14:
                    sheet['P39'] = General_Data['Nombre']
                elif hora >= 14 and hora < 22:
                    sheet['P40'] = General_Data['Nombre'] 
                else:
                    sheet['P41'] = General_Data['Nombre']   
                sheet['P42'] = General_Data['Fecha']
            elif dia_semana == 'Viernes':
                if hora >= 6 and hora < 14:
                    sheet['S39'] = General_Data['Nombre']
                elif hora >= 14 and hora < 22:
                    sheet['S40'] = General_Data['Nombre'] 
                else:
                    sheet['S41'] = General_Data['Nombre']   
                sheet['S42'] = General_Data['Fecha']
            elif dia_semana == 'Sábado':
                if hora >= 6 and hora < 14:
                    sheet['V39'] = General_Data['Nombre']
                elif hora >= 14 and hora < 22:
                    sheet['V40'] = General_Data['Nombre'] 
                else:
                    sheet['V41'] = General_Data['Nombre']   
                sheet['V42'] = General_Data['Fecha']
            else:
                if hora >= 6 and hora < 14:
                    sheet['Y39'] = General_Data['Nombre']
                elif hora >= 14 and hora < 22:
                    sheet['Y40'] = General_Data['Nombre'] 
                else:
                    sheet['Y41'] = General_Data['Nombre']   
                sheet['Y42'] = General_Data['Fecha']
            
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
        form = InspeccionForm(request.POST, request.FILES)
        print(request.POST) 
        if form.is_valid():
            Sheet = request.session.get('Sheet', None)
            if Sheet is None:
                return redirect('FormG')
            
            nombre_archivo = request.session.get('nombre_archivo')
            inspeccion = form.cleaned_data
            print(inspeccion)
            wb = load_workbook(filename= nombre_archivo)
            sheet = wb[Sheet]
            N=9
            
            if dia_semana == 'Lunes':
                
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            sheet['G'+str(N)] = value
                            sheet['H'+str(N)] = 'x'
                            sheet['I'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            
                            sheet['H'+str(N)] = value
                            sheet['I'+str(N)] = 'x'
                            sheet['G'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            
                            sheet['I'+str(N)] = value
                            sheet['G'+str(N)] = 'x'
                            sheet['H'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            sheet['G'+str(N)] = value
                            N+=1
            elif dia_semana == 'Martes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            
                            sheet['J'+str(N)] = value
                            sheet['K'+str(N)] = 'x'
                            sheet['L'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            
                            sheet['K'+str(N)] = value
                            sheet['L'+str(N)] = 'x'
                            sheet['J'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            
                            sheet['L'+str(N)] = value
                            sheet['J'+str(N)] = 'x'
                            sheet['K'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            sheet['J'+str(N)] = value
                            N+=1         
            elif dia_semana == 'Miércoles':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            
                            sheet['M'+str(N)] = value
                            sheet['N'+str(N)] = 'x'
                            sheet['O'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            
                            sheet['N'+str(N)] = value
                            sheet['O'+str(N)] = 'x'
                            sheet['M'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            
                            sheet['O'+str(N)] = value
                            sheet['M'+str(N)] = 'x'
                            sheet['N'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            sheet['M'+str(N)] = value
                            N+=1
            elif dia_semana == 'Jueves':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            
                            sheet['P'+str(N)] = value
                            sheet['Q'+str(N)] = 'x'
                            sheet['R'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            
                            sheet['Q'+str(N)] = value
                            sheet['R'+str(N)] = 'x'
                            sheet['P'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            
                            sheet['R'+str(N)] = value
                            sheet['P'+str(N)] = 'x'
                            sheet['Q'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            sheet['P'+str(N)] = value
                            N+=1
            elif dia_semana == 'Viernes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            
                            sheet['S'+str(N)] = value
                            sheet['T'+str(N)] = 'x'
                            sheet['U'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            
                            sheet['T'+str(N)] = value
                            sheet['U'+str(N)] = 'x'
                            sheet['S'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            
                            sheet['U'+str(N)] = value
                            sheet['S'+str(N)] = 'x'
                            sheet['T'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            sheet['S'+str(N)] = value
                            N+=1
            elif dia_semana == 'Sábado':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            
                            sheet['V'+str(N)] = value
                            sheet['W'+str(N)] = 'x'
                            sheet['X'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            
                            sheet['W'+str(N)] = value
                            sheet['X'+str(N)] = 'x'
                            sheet['V'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            
                            sheet['X'+str(N)] = value
                            sheet['V'+str(N)] = 'x'
                            sheet['W'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            sheet['V'+str(N)] = value
                            N+=1
            elif dia_semana == 'Domingo':
                   for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            
                            sheet['Y'+str(N)] = value
                            sheet['Z'+str(N)] = 'x'
                            sheet['AA'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            
                            sheet['Z'+str(N)] = value
                            sheet['AA'+str(N)] = 'x'
                            sheet['Y'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            
                            sheet['AA'+str(N)] = value
                            sheet['Y'+str(N)] = 'x'
                            sheet['Z'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            sheet['Y'+str(N)] = value
                            N+=1
                   
            wb.save(nombre_archivo)                   
                
            form.save()
            return redirect ('FormFP')
        else:
            Titulo = 'Formulario de Inspección.'
            error = 'Tienes que llenar todos los campos para continuar con el formulario.'
            form = InspeccionForm(request.POST, request.FILES)
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
        print(request.POST)
        
        if form.is_valid():
            Sheet = request.session.get('Sheet', None)
            if Sheet is None:
                return redirect('FormG')
            nombre_archivo = request.session.get('nombre_archivo')
            inspeccion = form.cleaned_data
            print(inspeccion)
            wb = load_workbook(filename= nombre_archivo)
            sheet = wb[Sheet]
            N=25
            
            if dia_semana == 'Lunes':
                
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            
                            sheet['G'+str(N)] = value
                            sheet['H'+str(N)] = 'x'
                            sheet['I'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            
                            sheet['H'+str(N)] = value
                            sheet['I'+str(N)] = 'x'
                            sheet['G'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            
                            sheet['I'+str(N)] = value
                            sheet['G'+str(N)] = 'x'
                            sheet['H'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            sheet['G'+str(N)] = value
                            N+=1
            elif dia_semana == 'Martes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            
                            sheet['J'+str(N)] = value
                            sheet['K'+str(N)] = 'x'
                            sheet['L'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            
                            sheet['K'+str(N)] = value
                            sheet['L'+str(N)] = 'x'
                            sheet['J'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            
                            sheet['L'+str(N)] = value
                            sheet['J'+str(N)] = 'x'
                            sheet['K'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            sheet['J'+str(N)] = value
                            N+=1         
            elif dia_semana == 'Miércoles':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            
                            sheet['M'+str(N)] = value
                            sheet['N'+str(N)] = 'x'
                            sheet['O'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            
                            sheet['N'+str(N)] = value
                            sheet['O'+str(N)] = 'x'
                            sheet['M'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            
                            sheet['O'+str(N)] = value
                            sheet['M'+str(N)] = 'x'
                            sheet['N'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            sheet['M'+str(N)] = value
                            N+=1
            elif dia_semana == 'Jueves':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            
                            
                            sheet['P'+str(N)] = value
                            sheet['Q'+str(N)] = 'x'
                            sheet['R'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            
                            
                            sheet['Q'+str(N)] = value
                            sheet['R'+str(N)] = 'x'
                            sheet['P'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            
                            
                            sheet['R'+str(N)] = value
                            sheet['P'+str(N)] = 'x'
                            sheet['Q'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            
                            sheet['P'+str(N)] = value
                            N+=1
            elif dia_semana == 'Viernes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            
                            sheet['S'+str(N)] = value
                            sheet['T'+str(N)] = 'x'
                            sheet['U'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            
                            sheet['T'+str(N)] = value
                            sheet['U'+str(N)] = 'x'
                            sheet['S'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            
                            sheet['U'+str(N)] = value
                            sheet['S'+str(N)] = 'x'
                            sheet['T'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            sheet['S'+str(N)] = value
                            N+=1
            elif dia_semana == 'Sábado':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            
                            sheet['V'+str(N)] = value
                            sheet['W'+str(N)] = 'x'
                            sheet['X'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            
                            sheet['W'+str(N)] = value
                            sheet['X'+str(N)] = 'x'
                            sheet['V'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            
                            sheet['X'+str(N)] = value
                            sheet['V'+str(N)] = 'x'
                            sheet['W'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            sheet['V'+str(N)] = value
                            N+=1
            elif dia_semana == 'Domingo':
                   for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            
                            sheet['Y'+str(N)] = value
                            sheet['Z'+str(N)] = 'x'
                            sheet['AA'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            
                            sheet['Z'+str(N)] = value
                            sheet['AA'+str(N)] = 'x'
                            sheet['Y'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            
                            sheet['AA'+str(N)] = value
                            sheet['Y'+str(N)] = 'x'
                            sheet['Z'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            sheet['Y'+str(N)] = value
                            N+=1
                   
            wb.save(nombre_archivo)                   
                
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
        print(request.POST)
        
        if form.is_valid():
            Sheet = request.session.get('Sheet', None)
            if Sheet is None:
                return redirect('FormG')
            nombre_archivo = request.session.get('nombre_archivo')
            inspeccion = form.cleaned_data
            print(inspeccion)
            wb = load_workbook(filename= nombre_archivo)
            sheet = wb[Sheet]
            N=29
            
            if dia_semana == 'Lunes':
                
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            
                            sheet['G'+str(N)] = value
                            sheet['H'+str(N)] = 'x'
                            sheet['I'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            
                            sheet['H'+str(N)] = value
                            sheet['I'+str(N)] = 'x'
                            sheet['G'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            
                            sheet['I'+str(N)] = value
                            sheet['G'+str(N)] = 'x'
                            sheet['H'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            sheet['G'+str(N)] = value
                            N+=1
            elif dia_semana == 'Martes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            
                            sheet['J'+str(N)] = value
                            sheet['K'+str(N)] = 'x'
                            sheet['L'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            
                            sheet['K'+str(N)] = value
                            sheet['L'+str(N)] = 'x'
                            sheet['J'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            
                            sheet['L'+str(N)] = value
                            sheet['J'+str(N)] = 'x'
                            sheet['K'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            sheet['J'+str(N)] = value
                            N+=1         
            elif dia_semana == 'Miércoles':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            
                            sheet['M'+str(N)] = value
                            sheet['N'+str(N)] = 'x'
                            sheet['O'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            
                            sheet['N'+str(N)] = value
                            sheet['O'+str(N)] = 'x'
                            sheet['M'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            
                            sheet['O'+str(N)] = value
                            sheet['M'+str(N)] = 'x'
                            sheet['N'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            sheet['M'+str(N)] = value
                            N+=1
            elif dia_semana == 'Jueves':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            
                            
                            sheet['P'+str(N)] = value
                            sheet['Q'+str(N)] = 'x'
                            sheet['R'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            
                            
                            sheet['Q'+str(N)] = value
                            sheet['R'+str(N)] = 'x'
                            sheet['P'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            
                            
                            sheet['R'+str(N)] = value
                            sheet['P'+str(N)] = 'x'
                            sheet['Q'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            
                            sheet['P'+str(N)] = value
                            N+=1
            elif dia_semana == 'Viernes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            
                            sheet['S'+str(N)] = value
                            sheet['T'+str(N)] = 'x'
                            sheet['U'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            
                            sheet['T'+str(N)] = value
                            sheet['U'+str(N)] = 'x'
                            sheet['S'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            
                            sheet['U'+str(N)] = value
                            sheet['S'+str(N)] = 'x'
                            sheet['T'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            sheet['S'+str(N)] = value
                            N+=1
            elif dia_semana == 'Sábado':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            
                            sheet['V'+str(N)] = value
                            sheet['W'+str(N)] = 'x'
                            sheet['X'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            
                            sheet['W'+str(N)] = value
                            sheet['X'+str(N)] = 'x'
                            sheet['V'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            
                            sheet['X'+str(N)] = value
                            sheet['V'+str(N)] = 'x'
                            sheet['W'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            sheet['V'+str(N)] = value
                            N+=1
            elif dia_semana == 'Domingo':
                   for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            
                            sheet['Y'+str(N)] = value
                            sheet['Z'+str(N)] = 'x'
                            sheet['AA'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            
                            sheet['Z'+str(N)] = value
                            sheet['AA'+str(N)] = 'x'
                            sheet['Y'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            
                            sheet['AA'+str(N)] = value
                            sheet['Y'+str(N)] = 'x'
                            sheet['Z'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            sheet['Y'+str(N)] = value
                            N+=1
                   
            wb.save(nombre_archivo)                   
                
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
        
def generate_columns(start, end):
    letters = list(string.ascii_uppercase)
    columns = letters[letters.index(start):]
    if end in letters:
        columns += [f'A{letter}' for letter in letters[:letters.index(end)+1]]
    return columns

def FormBP(request):
    if request.method == 'POST':
        form = BackPartForm(request.POST, request.FILES)
        print(request.POST)
        
        if form.is_valid():
            Sheet = request.session.get('Sheet', None)
            if Sheet is None:
                return redirect('FormG')
            Ruta = request.session.get('Ruta')
            nombre_archivo = request.session.get('nombre_archivo')
            inspeccion = form.cleaned_data
            print(inspeccion)
            wb = load_workbook(filename= nombre_archivo)
            sheet = wb[Sheet]
            N=34
            
            columnas = ['LUNESC', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA']
            
            if dia_semana == 'Lunes':
                
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            
                            sheet['G'+str(N)] = value
                            sheet['H'+str(N)] = 'x'
                            sheet['I'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            
                            sheet['H'+str(N)] = value
                            sheet['I'+str(N)] = 'x'
                            sheet['G'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            
                            sheet['I'+str(N)] = value
                            sheet['G'+str(N)] = 'x'
                            sheet['H'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            
                            sheet['G'+str(N)] = value
                            N+=1
            elif dia_semana == 'Martes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            
                            sheet['J'+str(N)] = value
                            sheet['K'+str(N)] = 'x'
                            sheet['L'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            
                            sheet['K'+str(N)] = value
                            sheet['L'+str(N)] = 'x'
                            sheet['J'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            
                            sheet['L'+str(N)] = value
                            sheet['J'+str(N)] = 'x'
                            sheet['K'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            
                            sheet['J'+str(N)] = value
                            N+=1
            elif dia_semana == 'Miércoles':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            
                            sheet['M'+str(N)] = value
                            sheet['N'+str(N)] = 'x'
                            sheet['O'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            
                            sheet['N'+str(N)] = value
                            sheet['O'+str(N)] = 'x'
                            sheet['M'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            
                            sheet['O'+str(N)] = value
                            sheet['M'+str(N)] = 'x'
                            sheet['N'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            
                            sheet['M'+str(N)] = value
                            N+=1
            elif dia_semana == 'Jueves':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            
                            
                            sheet['P'+str(N)] = value
                            sheet['Q'+str(N)] = 'x'
                            sheet['R'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            
                            
                            sheet['Q'+str(N)] = value
                            sheet['R'+str(N)] = 'x'
                            sheet['P'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            
                            
                            sheet['R'+str(N)] = value
                            sheet['P'+str(N)] = 'x'
                            sheet['Q'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            
                            sheet['P'+str(N)] = value
                            N+=1
            elif dia_semana == 'Viernes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            
                            sheet['S'+str(N)] = value
                            sheet['T'+str(N)] = 'x'
                            sheet['U'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            
                            sheet['T'+str(N)] = value
                            sheet['U'+str(N)] = 'x'
                            sheet['S'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            
                            sheet['U'+str(N)] = value
                            sheet['S'+str(N)] = 'x'
                            sheet['T'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            
                            sheet['S'+str(N)] = value
                            N+=1
            elif dia_semana == 'Sábado':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            
                            sheet['V'+str(N)] = value
                            sheet['W'+str(N)] = 'x'
                            sheet['X'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            
                            sheet['W'+str(N)] = value
                            sheet['X'+str(N)] = 'x'
                            sheet['V'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            
                            sheet['X'+str(N)] = value
                            sheet['V'+str(N)] = 'x'
                            sheet['W'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            
                            sheet['V'+str(N)] = value
                            N+=1
            elif dia_semana == 'Domingo':
                   for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            
                            sheet['Y'+str(N)] = value
                            sheet['Z'+str(N)] = 'x'
                            sheet['AA'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            
                            sheet['Z'+str(N)] = value
                            sheet['AA'+str(N)] = 'x'
                            sheet['Y'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            
                            sheet['AA'+str(N)] = value
                            sheet['Y'+str(N)] = 'x'
                            sheet['Z'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            
                            sheet['Y'+str(N)] = value
                            N+=1
            
            try:
                df_original = pd.read_excel(f'C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/{Ruta}/Copy.xlsx')
                df_curr = pd.read_excel(nombre_archivo) 

                pd.set_option('display.max_columns', None)
                pd.set_option('display.max_rows', None)

                print(df_curr)
                print(df_original)
                      
                for col in columnas:
                    if col in df_original.columns:
                        print(f'La columna {col} existe en el DataFrame.')
                    else:
                        print(f'La columna {col} no existe en el DataFrame.')
                        df = pd.read_csv('data.csv')
                        print(df)
                df_original_selected = df_original.loc[columnas]
                df_curr_selected = df_curr.loc[columnas]
                df_changes = df_curr_selected != df_original_selected
                
                df_changes['Combined'] = df_changes.apply(lambda row: ', '.join([f'{col}: {df_curr.loc[row.name, col]}' for col in columnas if row[col]]), axis=1)
                
                
                with pd.ExcelWriter(nombre_archivo, mode='a') as writer:
                    df_changes.to_excel(writer, sheet_name='Changes')
                
                wb.save(nombre_archivo)                      
                form.save()
            except FileNotFoundError:
                wb.save(nombre_archivo)                      
                form.save()
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
        