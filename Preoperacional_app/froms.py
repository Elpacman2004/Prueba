from django import forms
from .models import Datos_generales, Inspeccion

class DatosGeneralesForm(forms.ModelForm):
    class Meta:
        model = Datos_generales
        fields = ['Fecha', 'Proyecto', 'Nombre']

class InspeccionForm(forms.ModelForm):
    OPCIONES = [
        ('C', 'Cumple'),
        ('NC', 'No Cumple'),
        ('NA', 'No Aplica'),
    ]
    
    names = {
        'C': 'Cumple',
        'NC': 'No Cumple',
        'NA': 'No Aplica',
        }
    

    # Convertimos los campos booleanos a campos de elección
    Nivel_aceite = forms.ChoiceField(choices=OPCIONES, label='Nivel de aceite', widget=forms.RadioSelect)
    capot_asegurado = forms.ChoiceField(choices=OPCIONES, label='Capot asegurado', widget=forms.RadioSelect)

    class Meta:
        model = Inspeccion
        fields = [
            'vehiculo',
            'fecha',
            'Nivel_aceite',
            'capot_asegurado',
            'kilometraje_inicial',
            'Nivel_gasometro',
        ]
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

