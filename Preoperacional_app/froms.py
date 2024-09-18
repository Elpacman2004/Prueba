from django import forms
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import Datos_generales, Inspeccion, FrontPart, Side, BackPart, ED_LI
from Hoja_de_vida_vehiculo.models import General_data
from dal import autocomplete
from dal_select2.widgets import ModelSelect2

class DatosGeneralesForm(forms.ModelForm):
    
    vehiculo = forms.CharField(max_length=200)    
    class Meta:
        
        model = Datos_generales
        fields = ['Fecha', 'Proyecto', 'Nombre', 'vehiculo', 'Origen', 'Destino']
        widgets = {
            'Proyecto': forms.TextInput(attrs={
                'placeholder': 'PP-Proyecto-Año',
                'class': 'form-control',
                'id': 'inputProyecto',
                'aria-describedby': 'proyectoHelpBlock'
            }),

            'Origen': forms.TextInput(attrs={
                'placeholder': 'Ej: Cl. 21 #69B-74',
                'class': 'form-control',
                'id': 'inputProyecto',
                'aria-describedby': 'proyectoHelpBlock'
            }),

            'Destino': forms.TextInput(attrs={
                'placeholder': 'Ej: Cl. 95 #89B-27',
                'class': 'form-control',
                'id': 'inputProyecto',
                'aria-describedby': 'proyectoHelpBlock'
            }),

            'Fecha': forms.DateInput(attrs={
                'class': 'form-control-plaintext',
                'id': 'staticFecha',
                'readonly': 'readonly',
            }),
        }
                                     
        help_texts = {
            'Proyecto': 'Debes colocar el proyecto y el año en el formato PP-Proyecto-Año. Ejemplo: PP-001-2021',
        }
        
    def clean_vehiculo(self):
        vehiculo_str = self.cleaned_data.get('vehiculo')
        try:
            vehiculo_instance = General_data.objects.get(License_plate=vehiculo_str)
        except ObjectDoesNotExist:
            self.add_error('vehiculo', "El vehículo con placa {} no existe.".format(vehiculo_str))
            return None
        return vehiculo_instance

class InspeccionForm(forms.ModelForm):
    class Meta:
        model = Inspeccion
        fields = [
            'Nivel_aceite',
            'capot_asegurado',
            'bornes_baterias_ajustados',
            'indicadores_tablero_control',
            'kilometraje_inicial',
            'aire_acondicionado',
            'freno_estacionamiento',
            'limpiaparabrisas',
            'pito_electrico',
            'cinturones_seguridad',
            'equipo_prevencion_seguridad',
            'botiquin_primeros_auxilios',
            'extintor',
            'kit_derrames',
            'sensor_externo_velocidad',
            'Nivel_del_combustible',
        ]
        
        widgets = {
            'Nivel_del_combustible': forms.ClearableFileInput(attrs={
                'capture': 'camera',
            }),
        }  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

class ED_LIForm(forms.ModelForm):
    class Meta:
        model = ED_LI
        fields = ['First_Aid_Kit_LI', 'Fire_Extinguisher_ED', 'Spill_Kit_LI']

class InspeccionForm_ED_LI(forms.Form):
    Nivel_aceite = forms.CharField()
    capot_asegurado = forms.CharField()
    bornes_baterias_ajustados = forms.CharField()
    indicadores_tablero_control = forms.CharField()
    kilometraje_inicial = forms.IntegerField()
    aire_acondicionado = forms.CharField()
    freno_estacionamiento = forms.CharField()
    limpiaparabrisas = forms.CharField()
    pito_electrico = forms.CharField()
    cinturones_seguridad = forms.CharField()
    equipo_prevencion_seguridad = forms.CharField()
    botiquin_primeros_auxilios = forms.CharField()
    First_Aid_Kit_LI = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    extintor = forms.CharField()
    Fire_Extinguisher_ED = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    kit_derrames = forms.CharField()
    Spill_Kit_LI = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    sensor_externo_velocidad = forms.CharField()
    Nivel_del_combustible = forms.FileField(widget=forms.ClearableFileInput(attrs={'capture': 'camera'}))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['First_Aid_Kit_LI'].label = 'Botiquín de primeros auxilios última inspección'
        self.fields['Fire_Extinguisher_ED'].label = 'Extintor fecha de vencimiento'
        self.fields['Spill_Kit_LI'].label = 'Kit de derrames última inspección'

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            
class FrontPartForm (forms.ModelForm):

    class Meta:
        model = FrontPart
        fields = [
            'funcionamiento_luces_delanteras',
            'vidrio_delantero_sin_fisuras',
            'placa_delantera_legible',
            'Labrado_de_las_llantas_delanteras',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'  

class SideForm (forms.ModelForm):

    class Meta:
        model = Side
        fields = [
            'carroceria_buen_estado',
            'vidrios_laterales_sin_fisuras',
            'direccionales_funcionando',
            'espejo_exterior_buen_estado',
            'sin_fugas_tanque_combustible',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            
class BackPartForm (forms.ModelForm):

    class Meta:
        model = BackPart
        fields = [   
            'luces_traseras_funcionando',
            'sonido_alarma_reversa',
            'labrado_llantas_traseras',
            'labrado_llanta_repuesto',
            'placa_trasera_legible',
            'Obser',
        ]
        
        labels = {
            'Obser': 'Observaciones',
        }
        
        widgets = {
            'Obser': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'