from django .shortcuts import render, redirect
from .froms import DatosGeneralesForm, InspeccionForm
from .models import Datos_generales, Inspeccion, Vehiculo
from django.http import Http404

def index(request):
    return render(request, 'Index.html')

def FormG (request):
    if request.method == 'POST':
        
        Form = DatosGeneralesForm(request.POST, request.FILES)
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
        print(request.POST)
        if form.is_valid:
            
            form.save()
            return redirect ('Index')
    
    else:
        form = InspeccionForm()
        return render(request, 'Forms/Formpruebas.html', {'form': form})
    

