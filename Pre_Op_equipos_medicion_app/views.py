from django.shortcuts import render, redirect
from .forms import EquipmentInspection_form
from .Signatures import Proces_signatures
from openpyxl import load_workbook
from datetime import datetime
from openpyxl.drawing.image import Image as OpenpyxlImage
import shutil
from PIL import Image as PILImage

def PreOp_equpment(request):
    if request.method == 'POST':
        form = EquipmentInspection_form(request.POST)
        if form.is_valid():
                date_str = datetime.now().strftime('%Y-%m-%d')
                PreOp_data = form.cleaned_data

                new_file_name = f"C:/Users/Dagelec LTDA/Desktop/Eco_forms/Eco_forms/Pruebas_excel/Pre-Operacional de equipos/{str(PreOp_data['id_eqipment'])}_{date_str}.xlsx"
                shutil.copy('C:/Users/Dagelec LTDA/Desktop/Eco_forms/Eco_forms/Pruebas_excel/Plantilla_PreOp_Equpo_de_medicion.xlsx', new_file_name)

                wb = load_workbook(filename= new_file_name)
                sheet = wb['Preoperacional Equipo de Prueba']

                sheet['B7'] = PreOp_data['place']
                sheet['B8'] = PreOp_data['id_eqipment']
                sheet['B9'] = PreOp_data['date']
                sheet['B10'] = PreOp_data['brand']
                sheet['B11'] = PreOp_data['serial']

                inspections = [
                     'visual_check', 'loose_fasteners', 'power_connections_ok', 'power_button_ok', 'fuses_ok', 'power_cable_ok', 'noises', 'loose_parts', 'temp_humidity', 'display_ok', 'other_components_ok', 'current_cable', 'voltage_cables', 'measurement_cables', 'ac_voltage_outputs', 'dc_current_outputs', 'ac_current_outputs', 'ac_voltage_input', 'dc_voltage_input', 'resistance_measurement',
                ]

                row = 14
                C_colum = 'J'
                NC_colum = 'K'
                NA_colum = 'L' 
                for i, inspection in enumerate(inspections):
                    sheet[f'{C_colum}{row}'] = 'X' if PreOp_data[inspection] == 'Cumple' else ''
                    sheet[f'{NC_colum}{row}'] = 'X' if PreOp_data[inspection] == 'No cumple' else ''
                    sheet[f'{NA_colum}{row}'] = 'X' if PreOp_data[inspection] == 'No aplica' else ''
                    row += 1
                    if row > 22 and C_colum == 'J':
                        row = 14
                        C_colum = 'W'
                        NC_colum = 'X'
                        NA_colum = 'Y' 

                sheet['A26'] = PreOp_data['notes']
                sheet['A36'] = PreOp_data['recommendations']

                
                Proces_signatures(request, sheet)

                wb.save(new_file_name)
                return redirect('Index')
    else:
        Form = EquipmentInspection_form()
        Title = 'Formulario de inspaccion pre-operacional de equipos de medicion'
        return render(request, 'PreOp_equpment.html', {'Title': Title, 'form': Form})