from django.shortcuts import render, redirect
from .froms import DatosGeneralesForm, InspeccionForm, ParteDelanteraForm, CostadoForm, ParteTraseraForm
from .models import Datos_generales, Inspeccion

# Create your views here.
def index(request):
    return render(request, 'Index.html')

def FormG(request):
    if request.method == 'POST':
       form = DatosGeneralesForm(request.POST)
       if form.is_valid():
           print (request.POST)
           form.save()
           return redirect ('InspectionForm') 
    else:
        form = DatosGeneralesForm()
        return render(request, 'Forms/FormG.html', {'form': form})
        
def FormI(request):
    if request.method == 'POST':
        form = InspeccionForm(request.POST, request.FILES)  # Manejar archivos con request.FILES
        if form.is_valid():
            print (request.POST)
            print(form.cleaned_data)
            form.save()
            print("Registro guardado correctamente.")
            return redirect('FormFP')

    else:
        form = InspeccionForm()
    return render(request, 'Forms/FirstForm.html', {'form': form})

    return 
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