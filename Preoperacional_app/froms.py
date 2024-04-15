from django import forms
from .models import Datos_generales, Inspeccion, ParteDelantera, Costado, ParteTrasera

class DatosGeneralesForm(forms.ModelForm):
    class Meta:
        model = Datos_generales
        fields = ['Fecha', 'Proyecto', 'Nombre']
        

class InspeccionForm(forms.ModelForm):
    class Meta:
        model = Inspeccion
        fields = [
            'vehiculo',
            'fecha',
            'Nivel_aceite',
            'kilometraje_inicial',
            'Nivel_gasometro',
        ]
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'



class ParteDelanteraForm(forms.ModelForm):
    class Meta:
        model = ParteDelantera
        fields = ['funcionamiento_luces_delanteras', 'vidrio_delantero_sin_fisuras', 'placa_delantera_legible']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

class CostadoForm(forms.ModelForm):
    class Meta:
        model = Costado
        fields = ['carroceria_buen_estado', 'vidrios_laterales_sin_fisuras', 'direccionales_funcionando', 'espejo_exterior_buen_estado', 'sin_fugas_tanque_combustible']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

class ParteTraseraForm(forms.ModelForm):
    class Meta:
        model = ParteTrasera
        fields = ['luces_traseras_funcionando', 'sonido_alarma_reversa', 'labrado_llantas_traseras', 'labrado_llanta_repuesto', 'placa_trasera_legible']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'