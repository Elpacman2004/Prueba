from django.shortcuts import render
from .forms import EquipmentInspection_form

def PreOp_equpment(request):
    if request.method == 'POST':
        pass
    else:
        Form = EquipmentInspection_form()
        Title = 'Formulario de inspaccion pre-operacional de equipos de medicion'
        return render(request, 'PreOp_equpment.html', {'Title': Title, 'form': Form})
