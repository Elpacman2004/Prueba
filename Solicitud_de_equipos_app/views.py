from django.shortcuts import render, redirect
from .forms import GeneralDataSEForm, EquipmentForm, Tools_and_Accessories_form, SafetyEquipmentForm, VehicleLogisticsForm, SearchForm
from .models import Equipment
from django.http import JsonResponse
from django.db.models import Q
from django.apps import apps
from django.core import serializers


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
            print('\nFormulario valido\n')
            print(f'\n{form.cleaned_data}\n')
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
            print('\nFormulario valido\n')
            print(f'\n{form.cleaned_data}\n')
            return redirect('ToolsAndAccessories')
    else:
        title = 'Equipos.'
        query = request.GET.get('q', '')
        if query:
            return redirect('search', model_name='Equipment')
        return render(request, 'Forms.html', {
            'model_name': 'Equipment',
            'form': form,
            'title': title,
            })
    
def ToolsAndAccessories (request):
    if request.method == 'POST':
        form = Tools_and_Accessories_form(request.POST)
        if form.is_valid():
            print('\nFormulario valido\n')
            print(f'\n{form.cleaned_data}\n')
            return redirect('SafetyEquipment')
    else:
        forn =Tools_and_Accessories_form
        title = 'Herramientas y accesorios.'
        return render(request, 'Forms.html', {
            'form': form,
            'title': title,
            })
        
def SafetyEquipment_view (request):
    if request.method == 'POST':
        form = SafetyEquipmentForm(request.POST)
        if form.is_valid():
            print('\nFormulario valido\n')
            print(f'\n{form.cleaned_data}\n')
            return redirect('VehicleLogistics')
    else:
        form = SafetyEquipmentForm()
        title = 'Equipos de seguridad.'
        return render(request, 'Forms.html', {
            'form': form,
            'title': title,
            })
        
def VehicleLogistics_view (request):
    if request.method == 'POST':
        form = VehicleLogisticsForm(request.POST)
        if form.is_valid():
            print('\nFormulario valido\n')
            print(f'\n{form.cleaned_data}\n')
            return redirect('IndexSE')
    else:
        form = VehicleLogisticsForm()
        title = 'Logistica de vehiculos.'
        return render(request, 'Forms.html', {
            'form': form,
            'title': title,
            })