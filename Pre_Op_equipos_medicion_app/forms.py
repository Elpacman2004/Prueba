from django import forms
from .models import EquipmentInspection

class EquipmentInspection_form(forms.ModelForm):

    Choises = [
        ('Cumple', 'Cumple'),
        ('No cumple', 'No cumple'),
        ('No aplica', 'No aplica'),
    ]

    visual_check = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Inspección visual')
    loose_fasteners = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Clavos, tornillos, astillas, tuercas salidas')
    power_connections_ok = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Conexiones de alimentacion estan en buen estado')
    power_button_ok = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Equipo enciende pulsador de encendido/apagado en buen estado')
    fuses_ok = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Fusibles completos')
    power_cable_ok = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Cable de poder en buen estado')
    noises = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Ruidos Extraños')
    loose_parts = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Elementos sueltos')
    temp_humidity = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Verificar temperatura del equipo en°C y humedad')
    display_ok = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Display en buen estado')
    other_components_ok = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Otros componentes del equipo estan en buen estado')
    current_cable = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Cable de Corrientes(800A)')
    voltage_cables = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Cables de tension_(2_kV)')
    measurement_cables = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Cables de medida')
    ac_voltage_outputs = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Verificación salidas de tensión AC')
    dc_current_outputs = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Verificación salidas de corriente DC')
    ac_current_outputs = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Verificación salidas de corriente AC')
    ac_voltage_input = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Verificación entrada de tensión AC')
    dc_voltage_input = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Verificación entrada de tensión DC')
    dc_current_input = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Verificación entrada de corriente DC')
    ac_current_input = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Verificación entrada de corriente AC')
    resistance_measurement = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class': 'Radios'}), label='Verificación medida de resistencia')

    class Meta:
        model = EquipmentInspection
        fields = [
            'place', 
            'id', 
            'date', 
            'brand', 
            'serial', 
            'visual_check', 
            'loose_fasteners', 
            'power_connections_ok', 
            'power_button_ok', 
            'fuses_ok', 
            'power_cable_ok', 
            'noises', 
            'loose_parts', 
            'temp_humidity', 
            'display_ok', 
            'other_components_ok', 
            'current_cable', 
            'voltage_cables', 
            'measurement_cables', 
            'ac_voltage_outputs', 
            'dc_current_outputs', 
            'ac_current_outputs', 
            'ac_voltage_input', 
            'dc_voltage_input', 
            'dc_current_input', 
            'ac_current_input', 
            'resistance_measurement', 
            'notes'
        ]

        labels = {
            'place': 'Localización',
            'id_eqipment': 'Identificacion interna',
            'date': 'Fecha de inspección',
            'brand': 'Marca',
            'serial': 'Serie',
            'visual_check': 'Inspección visual',
            'loose_fasteners': 'Clavos, tornillos, astillas, tuercas salidas',
            'power_connections_ok': 'Conexiones de alimentacion estan en buen estado',
            'power_button_ok': 'Equipo enciende pulsador de encendido/apagado en buen estado',
            'fuses_ok': 'Fusibles completos',
            'power_cable_ok': 'Cable de poder en buen estado',
            'noises': 'Ruidos Extraños',
            'loose_parts': 'Elementos sueltos',
            'temp_humidity': 'Verificar temperatura del equipo en°C y humedad',
            'display_ok': 'Display en buen estado',
            'other_components_ok': 'Otros componentes del equipo estan en buen estado',
            'current_cable': 'Cable de Corrientes(800A)',
            'voltage_cables': 'Cables de tension_(2_kV)',
            'measurement_cables': 'Cables de medida',
            'ac_voltage_outputs': 'Verificación salidas de tensión AC',
            'dc_current_outputs': 'Verificación salidas de corriente DC',
            'ac_current_outputs': 'Verificación salidas de corriente AC',
            'ac_voltage_input': 'Verificación entrada de tensión AC',
            'dc_voltage_input': 'Verificación entrada de tensión DC',
            'dc_current_input': 'Verificación entrada de corriente DC',
            'ac_current_input': 'Verificación entrada de corriente AC',
            'resistance_measurement': 'Verificación medida de resistencia',
            'notes': 'Observaciones',
        }

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }