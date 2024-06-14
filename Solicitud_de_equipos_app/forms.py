from django import forms
from .models import General_dataSE, Equipment, Tools_and_Accessories, SafetyEquipment, VehicleLogistics

class GeneralDataSEForm(forms.ModelForm):
    class Meta:
        model = General_dataSE
        fields = '__all__'
        
        labels = {
            'City': 'Ciudad',
            'Date': 'Fecha',
            'Name_project': 'Nombre del proyecto',
            'Supervisor': 'Supervisor',
            'Project_code': 'Código del proyecto',
            'Client': 'Cliente',
            'Location': 'Locación',
        }
        
        widgets = {
            'Date': forms.DateInput(attrs={'type': 'date'}),
        }
        
class SearchForm(forms.Form):
    column = forms.CharField(max_length=200, required=False, label='Seleccion de campos')

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'

class Tools_and_Accessories_form(forms.ModelForm):
    class Meta:
        model = Tools_and_Accessories
        fields = '__all__'

class SafetyEquipmentForm(forms.ModelForm):
    class Meta:
        model = SafetyEquipment
        fields = '__all__'

class VehicleLogisticsForm(forms.ModelForm):
    class Meta:
        model = VehicleLogistics
        fields = '__all__'
        
        widgets = {
            'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
            'fecha_entrada': forms.DateInput(attrs={'type': 'date'}),   
        }