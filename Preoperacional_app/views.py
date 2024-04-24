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


hoy = datetime.now()

dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
dia_semana = dias_semana[hoy.weekday()]
date_str = datetime.now().strftime('%Y-%m-%d')


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
                
                now = timezone.now()
                days_passed = (now - ultimo_archivo.created_at).days
                if days_passed == 7 or 14 or 21:
                    wb = load_workbook(filename= nombre_archivo)
                    if days_passed ==7:
                        ws = wb.create_sheet("Semana 2")
                    elif days_passed == 14:
                        ws = wb.create_sheet("Semana 3")
                    elif days_passed == 21:
                        ws = wb.create_sheet("Semana 4")
                elif days_passed == 30:
                    new_file_name = f"C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/{str(General_Data['vehiculo'])}_{date_str}.xlsx"
                    shutil.copy('C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/Plantilla.xlsx', new_file_name)
                    Historial = Histoial_archivos.objects.create(vehiculo = General_Data['vehiculo'], Nombre_archivo = new_file_name)
                    Historial.save()
                    wb = load_workbook(filename= new_file_name)
                    request.session['nombre_archivo'] = new_file_name
                else:
                    nombre_archivo = ultimo_archivo.Nombre_archivo
                    wb = load_workbook(filename= nombre_archivo)
                    request.session['nombre_archivo'] = nombre_archivo
            else:               
                new_file_name = f"C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/{str(General_Data['vehiculo'])}_{date_str}.xlsx"
                shutil.copy('C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/Plantilla.xlsx', new_file_name)
                Historial = Histoial_archivos.objects.create(vehiculo = General_Data['vehiculo'], Nombre_archivo = new_file_name)
                Historial.save()
                wb = load_workbook(filename= new_file_name)
                request.session['nombre_archivo'] = new_file_name
                
            sheet = wb['MySheet']
            sheet['E5'] = str(General_Data['vehiculo'])
            sheet['U5'] = General_Data['Proyecto']
            if dia_semana == 'Lunes':
                sheet['G39'] = General_Data['Nombre']
                sheet['G40'] = General_Data['Fecha']
            elif dia_semana == 'Martes':
                sheet['J39'] = General_Data['Nombre']
                sheet['J40'] = General_Data['Fecha']
            elif dia_semana == 'Miércoles':
                sheet['M39'] = General_Data['Nombre']
                sheet['M40'] = General_Data['Fecha']
            elif dia_semana == 'Jueves':
                sheet['P39'] = General_Data['Nombre']
                sheet['P40'] = General_Data['Fecha']
            elif dia_semana == 'Viernes':
                sheet['S39'] = General_Data['Nombre']
                sheet['S40'] = General_Data['Fecha']
            elif dia_semana == 'Sábado':
                sheet['V39'] = General_Data['Nombre']
                sheet['V40'] = General_Data['Fecha']
            else:
                sheet['Y39'] = General_Data['Nombre']
                sheet['Y40'] = General_Data['Fecha']
            
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
            nombre_archivo = request.session.get('nombre_archivo')
            inspeccion = form.cleaned_data
            print(inspeccion)
            wb = load_workbook(filename= nombre_archivo)
            N=9
            
            if dia_semana == 'Lunes':
                
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['G'+str(N)] = value
                            sheet['H'+str(N)] = 'x'
                            sheet['I'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['H'+str(N)] = value
                            sheet['I'+str(N)] = 'x'
                            sheet['G'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['I'+str(N)] = value
                            sheet['G'+str(N)] = 'x'
                            sheet['H'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['G'+str(N)] = value
                            N+=1
            elif dia_semana == 'Martes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['J'+str(N)] = value
                            sheet['K'+str(N)] = 'x'
                            sheet['L'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['K'+str(N)] = value
                            sheet['L'+str(N)] = 'x'
                            sheet['J'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['L'+str(N)] = value
                            sheet['J'+str(N)] = 'x'
                            sheet['K'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['J'+str(N)] = value
                            N+=1         
            elif dia_semana == 'Miércoles':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['M'+str(N)] = value
                            sheet['N'+str(N)] = 'x'
                            sheet['O'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['N'+str(N)] = value
                            sheet['O'+str(N)] = 'x'
                            sheet['M'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['O'+str(N)] = value
                            sheet['M'+str(N)] = 'x'
                            sheet['N'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['M'+str(N)] = value
                            N+=1
            elif dia_semana == 'Jueves':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['P'+str(N)] = value
                            sheet['Q'+str(N)] = 'x'
                            sheet['R'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['Q'+str(N)] = value
                            sheet['R'+str(N)] = 'x'
                            sheet['P'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['R'+str(N)] = value
                            sheet['P'+str(N)] = 'x'
                            sheet['Q'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['P'+str(N)] = value
                            N+=1
            elif dia_semana == 'Viernes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['S'+str(N)] = value
                            sheet['T'+str(N)] = 'x'
                            sheet['U'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['T'+str(N)] = value
                            sheet['U'+str(N)] = 'x'
                            sheet['S'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['U'+str(N)] = value
                            sheet['S'+str(N)] = 'x'
                            sheet['T'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['S'+str(N)] = value
                            N+=1
            elif dia_semana == 'Sábado':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['V'+str(N)] = value
                            sheet['W'+str(N)] = 'x'
                            sheet['X'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['W'+str(N)] = value
                            sheet['X'+str(N)] = 'x'
                            sheet['V'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['X'+str(N)] = value
                            sheet['V'+str(N)] = 'x'
                            sheet['W'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['V'+str(N)] = value
                            N+=1
            elif dia_semana == 'Domingo':
                   for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['Y'+str(N)] = value
                            sheet['Z'+str(N)] = 'x'
                            sheet['AA'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['Z'+str(N)] = value
                            sheet['AA'+str(N)] = 'x'
                            sheet['Y'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['AA'+str(N)] = value
                            sheet['Y'+str(N)] = 'x'
                            sheet['Z'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
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
            nombre_archivo = request.session.get('nombre_archivo')
            inspeccion = form.cleaned_data
            print(inspeccion)
            wb = load_workbook(filename= nombre_archivo)
            N=25
            
            if dia_semana == 'Lunes':
                
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['G'+str(N)] = value
                            sheet['H'+str(N)] = 'x'
                            sheet['I'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['H'+str(N)] = value
                            sheet['I'+str(N)] = 'x'
                            sheet['G'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['I'+str(N)] = value
                            sheet['G'+str(N)] = 'x'
                            sheet['H'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['G'+str(N)] = value
                            N+=1
            elif dia_semana == 'Martes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['J'+str(N)] = value
                            sheet['K'+str(N)] = 'x'
                            sheet['L'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['K'+str(N)] = value
                            sheet['L'+str(N)] = 'x'
                            sheet['J'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['L'+str(N)] = value
                            sheet['J'+str(N)] = 'x'
                            sheet['K'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['J'+str(N)] = value
                            N+=1         
            elif dia_semana == 'Miércoles':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['M'+str(N)] = value
                            sheet['N'+str(N)] = 'x'
                            sheet['O'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['N'+str(N)] = value
                            sheet['O'+str(N)] = 'x'
                            sheet['M'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['O'+str(N)] = value
                            sheet['M'+str(N)] = 'x'
                            sheet['N'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['M'+str(N)] = value
                            N+=1
            elif dia_semana == 'Jueves':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['P'+str(N)] = value
                            sheet['Q'+str(N)] = 'x'
                            sheet['R'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['Q'+str(N)] = value
                            sheet['R'+str(N)] = 'x'
                            sheet['P'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['R'+str(N)] = value
                            sheet['P'+str(N)] = 'x'
                            sheet['Q'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['P'+str(N)] = value
                            N+=1
            elif dia_semana == 'Viernes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['S'+str(N)] = value
                            sheet['T'+str(N)] = 'x'
                            sheet['U'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['T'+str(N)] = value
                            sheet['U'+str(N)] = 'x'
                            sheet['S'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['U'+str(N)] = value
                            sheet['S'+str(N)] = 'x'
                            sheet['T'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['S'+str(N)] = value
                            N+=1
            elif dia_semana == 'Sábado':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['V'+str(N)] = value
                            sheet['W'+str(N)] = 'x'
                            sheet['X'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['W'+str(N)] = value
                            sheet['X'+str(N)] = 'x'
                            sheet['V'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['X'+str(N)] = value
                            sheet['V'+str(N)] = 'x'
                            sheet['W'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['V'+str(N)] = value
                            N+=1
            elif dia_semana == 'Domingo':
                   for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['Y'+str(N)] = value
                            sheet['Z'+str(N)] = 'x'
                            sheet['AA'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['Z'+str(N)] = value
                            sheet['AA'+str(N)] = 'x'
                            sheet['Y'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['AA'+str(N)] = value
                            sheet['Y'+str(N)] = 'x'
                            sheet['Z'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
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
            nombre_archivo = request.session.get('nombre_archivo')
            inspeccion = form.cleaned_data
            print(inspeccion)
            wb = load_workbook(filename= nombre_archivo)
            N=29
            
            if dia_semana == 'Lunes':
                
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['G'+str(N)] = value
                            sheet['H'+str(N)] = 'x'
                            sheet['I'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['H'+str(N)] = value
                            sheet['I'+str(N)] = 'x'
                            sheet['G'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['I'+str(N)] = value
                            sheet['G'+str(N)] = 'x'
                            sheet['H'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['G'+str(N)] = value
                            N+=1
            elif dia_semana == 'Martes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['J'+str(N)] = value
                            sheet['K'+str(N)] = 'x'
                            sheet['L'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['K'+str(N)] = value
                            sheet['L'+str(N)] = 'x'
                            sheet['J'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['L'+str(N)] = value
                            sheet['J'+str(N)] = 'x'
                            sheet['K'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['J'+str(N)] = value
                            N+=1         
            elif dia_semana == 'Miércoles':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['M'+str(N)] = value
                            sheet['N'+str(N)] = 'x'
                            sheet['O'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['N'+str(N)] = value
                            sheet['O'+str(N)] = 'x'
                            sheet['M'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['O'+str(N)] = value
                            sheet['M'+str(N)] = 'x'
                            sheet['N'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['M'+str(N)] = value
                            N+=1
            elif dia_semana == 'Jueves':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['P'+str(N)] = value
                            sheet['Q'+str(N)] = 'x'
                            sheet['R'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['Q'+str(N)] = value
                            sheet['R'+str(N)] = 'x'
                            sheet['P'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['R'+str(N)] = value
                            sheet['P'+str(N)] = 'x'
                            sheet['Q'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['P'+str(N)] = value
                            N+=1
            elif dia_semana == 'Viernes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['S'+str(N)] = value
                            sheet['T'+str(N)] = 'x'
                            sheet['U'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['T'+str(N)] = value
                            sheet['U'+str(N)] = 'x'
                            sheet['S'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['U'+str(N)] = value
                            sheet['S'+str(N)] = 'x'
                            sheet['T'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['S'+str(N)] = value
                            N+=1
            elif dia_semana == 'Sábado':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['V'+str(N)] = value
                            sheet['W'+str(N)] = 'x'
                            sheet['X'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['W'+str(N)] = value
                            sheet['X'+str(N)] = 'x'
                            sheet['V'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['X'+str(N)] = value
                            sheet['V'+str(N)] = 'x'
                            sheet['W'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['V'+str(N)] = value
                            N+=1
            elif dia_semana == 'Domingo':
                   for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['Y'+str(N)] = value
                            sheet['Z'+str(N)] = 'x'
                            sheet['AA'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['Z'+str(N)] = value
                            sheet['AA'+str(N)] = 'x'
                            sheet['Y'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['AA'+str(N)] = value
                            sheet['Y'+str(N)] = 'x'
                            sheet['Z'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
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

def FormBP(request):
    if request.method == 'POST':
        form = BackPartForm(request.POST, request.FILES)
        print(request.POST)
        
        if form.is_valid():
            nombre_archivo = request.session.get('nombre_archivo')
            inspeccion = form.cleaned_data
            print(inspeccion)
            wb = load_workbook(filename= nombre_archivo)
            N=34
            
            if dia_semana == 'Lunes':
                
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['G'+str(N)] = value
                            sheet['H'+str(N)] = 'x'
                            sheet['I'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['H'+str(N)] = value
                            sheet['I'+str(N)] = 'x'
                            sheet['G'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['I'+str(N)] = value
                            sheet['G'+str(N)] = 'x'
                            sheet['H'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['G'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['G'+str(N)] = value
                            N+=1
            elif dia_semana == 'Martes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['J'+str(N)] = value
                            sheet['K'+str(N)] = 'x'
                            sheet['L'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['K'+str(N)] = value
                            sheet['L'+str(N)] = 'x'
                            sheet['J'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['L'+str(N)] = value
                            sheet['J'+str(N)] = 'x'
                            sheet['K'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['J'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['J'+str(N)] = value
                            N+=1
            elif dia_semana == 'Miércoles':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['M'+str(N)] = value
                            sheet['N'+str(N)] = 'x'
                            sheet['O'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['N'+str(N)] = value
                            sheet['O'+str(N)] = 'x'
                            sheet['M'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['O'+str(N)] = value
                            sheet['M'+str(N)] = 'x'
                            sheet['N'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['M'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['M'+str(N)] = value
                            N+=1
            elif dia_semana == 'Jueves':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['P'+str(N)] = value
                            sheet['Q'+str(N)] = 'x'
                            sheet['R'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['Q'+str(N)] = value
                            sheet['R'+str(N)] = 'x'
                            sheet['P'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['R'+str(N)] = value
                            sheet['P'+str(N)] = 'x'
                            sheet['Q'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['P'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['P'+str(N)] = value
                            N+=1
            elif dia_semana == 'Viernes':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['S'+str(N)] = value
                            sheet['T'+str(N)] = 'x'
                            sheet['U'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['T'+str(N)] = value
                            sheet['U'+str(N)] = 'x'
                            sheet['S'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['U'+str(N)] = value
                            sheet['S'+str(N)] = 'x'
                            sheet['T'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['S'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['S'+str(N)] = value
                            N+=1
            elif dia_semana == 'Sábado':
                for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['V'+str(N)] = value
                            sheet['W'+str(N)] = 'x'
                            sheet['X'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['W'+str(N)] = value
                            sheet['X'+str(N)] = 'x'
                            sheet['V'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['X'+str(N)] = value
                            sheet['V'+str(N)] = 'x'
                            sheet['W'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['V'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['V'+str(N)] = value
                            N+=1
            elif dia_semana == 'Domingo':
                   for field, value in form.cleaned_data.items():
                    if value == 'C':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['Y'+str(N)] = value
                            sheet['Z'+str(N)] = 'x'
                            sheet['AA'+str(N)] = 'x'
                            N+=1
                    elif value == 'NC':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['Z'+str(N)] = value
                            sheet['AA'+str(N)] = 'x'
                            sheet['Y'+str(N)] = 'x'
                            N+=1
                    elif value == 'NA':
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            print (f'{field} - {value}')
                            sheet = wb['MySheet']
                            sheet['AA'+str(N)] = value
                            sheet['Y'+str(N)] = 'x'
                            sheet['Z'+str(N)] = 'x'
                            N+=1
                    else:
                        if isinstance(value, InMemoryUploadedFile):
                            sheet['Y'+str(N)] = value.name
                        else:
                            sheet = wb['MySheet']
                            sheet['Y'+str(N)] = value
                            N+=1
                   
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
        