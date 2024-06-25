from django import forms
from .models import GeneralDataDV, DFAD, IMC
from datetime import time
from django.core.exceptions import ObjectDoesNotExist

class GeneralDataDVForm(forms.ModelForm):
    CHOISES = [
        ('Equipment', 'Equipo'),
        ('Standard', 'Patrón '),
        ('Dielectric element', 'Elemento dielectrico'),
    ]
    
    Type_device = forms.ChoiceField(choices=CHOISES, widget=forms.RadioSelect, label='Tipo de dispositivo')
    
    class Meta:
        model = GeneralDataDV
        fields = 'NameD', 'Brand', 'Acquisition_Date', 'Supply_Voltage', 'RefModel', 'Supplier', 'Serial_number', 'Invoice', 'Type_device'
        labels = {
            'NameD': 'Nombre',
            'Brand': 'Marca',
            'Acquisition_Date': 'Fecha de adquisición',
            'Supply_Voltage': 'Tensión de alimentación',
            'RefModel': 'Referencia/Modelo',
            'Supplier': 'Proveedor',
            'Serial_number': 'Número de serie',
            'Invoice': 'Factura',
        }
        widgets = {
            'Acquisition_Date': forms.DateInput(attrs={'type': 'date'})
        }   

class DFADForm(forms.ModelForm):
    Photograph = forms.ImageField()
    
    class Meta:
        model = DFAD
        fields = 'Equipment_description', 'Photograph', 'Observations'
        labels = {
            'Equipment_description': 'Descripción del equipo',
            'Photograph': 'Fotografía',
            'Observations': 'Observaciones',
        }
        widgets = {
            'Equipment_description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
            'Photograph': forms.ClearableFileInput(attrs={
                'capture': 'camera',
            }),
        }
        
        
        
        
class IMC_form (forms.ModelForm):
    CHOISEST = [
        ('I', 'Inspeccion'),
        ('P', 'Mantenimiento preventivo'),
        ('C', 'Mantenimiento correctivo'),
        ('CA', 'Calibracion'),
    ]
    
    CHOISESR = [
        ('Si', 'Si'),
        ('No', 'No'),   
    ]
    
    Activity_type = forms.ChoiceField(choices=CHOISEST, widget=forms.RadioSelect, label='Tipo de actividad')
    Satisfactory_result = forms.ChoiceField(choices=CHOISESR, widget=forms.RadioSelect, label='Resultado satisfactorio')
    Device = forms.CharField(max_length=200, label='Dispositivo')
    
    class Meta:
        model = IMC
        fields = 'Device', 'Date', 'Activity_description', 'Activity_type', 'Certificate_docment_number', 'Satisfactory_result', 'Action_to_take', 'Next_revew', 'Frequency', 'Responsible'
        labels = {
            'Date': 'Fecha',
            'Activity_description': 'Descripción de la actividad',
            'Certificate_docment_number': 'Número de documento de certificado',
            'Satisfactory_result': 'Resultado satisfactorio',
            'Action_to_take': 'Acción a tomar',
            'Next_revew': 'Próxima revisión',
            'Frequency': 'Frecuencia',
            'Responsible': 'Responsable',
        }
        widgets = {
            'Date': forms.DateInput(attrs={'type': 'date'}),
            'Next_revew': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_Device(self):
            Device_str = self.cleaned_data.get('Device')
            try:
                Device_instance = GeneralDataDV.objects.get(NameD=Device_str)
            except ObjectDoesNotExist:
                raise forms.ValidationError("El dispositivo con el nombre {} no existe.".format(Device_str))
            return Device_instance