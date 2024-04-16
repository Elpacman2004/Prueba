from django .shortcuts import render, redirect
from .froms import DatosGeneralesForm, InspeccionForm, CostadoForm, ParteDelanteraForm, ParteTraseraForm, InspeccionFormNC, InspeccionFormNA
from .models import Datos_generales, Inspeccion, Vehiculo
from django.http import Http404

def index(request):
    return render(request, 'Index.html')

def FormG (request):
    if request.method == 'POST':
        
        Form = DatosGeneralesForm(request.POST)
        if Form.is_valid():
            print (request.POST)
            Form.save()
            return redirect('FormI')
    else:
        form = DatosGeneralesForm() 
        return render(request, 'Forms/FormG.html', {'form': form})

def FormI(request):
    if request.method == 'POST':
        form = InspeccionForm(request.POST, request.FILES)
        form_NC = InspeccionFormNC(request.POST, request.FILES)
        form_NA = InspeccionFormNA(request.POST, request.FILES)
        print (request.POST)
        
        if form.is_valid() and form_NC.is_valid() and form_NA.is_valid():
            
            print(form.cleaned_data)
            print(form_NC.cleaned_data)
            print(form_NA.cleaned_data)

            form.save()
            form_NC.save()
            form_NA.save()

    else:
        form = InspeccionForm()
        form_NC = InspeccionFormNC()
        form_NA = InspeccionFormNA()

    return render(request, 'Forms/FirstForm.html', {
        'form': form,
        'form_NC': form_NC,
        'form_NA': form_NA
    })


    

def FormFP (request):
    if request.method == 'GET':
        form = (ParteDelanteraForm)
        return render(request, 'Forms/FormFP.html', {'form': form})
    else:
        return redirect ('FormSP')

def FormSP (request):
    if request.method == 'GET':
        form = (CostadoForm)
        return render(request, 'Forms/FormSP.html', {'form': form})
    else:
        return redirect ('FormBP')

def FormBP (request):
    if request.method == 'GET':
        form = (ParteTraseraForm)
        return render(request, 'Forms/FormBP.html', {'form': form})
    else:
        return redirect ('Index')