from django import forms
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import General_data, Docments, Tecnical_specifications
from dal import autocomplete
from dal_select2.widgets import ModelSelect2

class General_data_form(forms.ModelForm):
    class Meta:
        model = General_data
        fields = [
            'License_plate',
            'Class',
            'Engine_number',
            'Chassis_number',
            'Brand',
            'Model',
            'Sevice',
            'Owner',
            'Line',
            'Body',
            'Color',
            'Docment',
        ]
        labels = {
            'License_plate': 'Placa',
            'Class': 'Clase',
            'Engine_number': 'Número de motor',
            'Chassis_number': 'Número de chasis',   
            'Brand': 'Marca',
            'Model': 'Modelo',
            'Sevice': 'Servicio',
            'Owner': 'Propietario',
            'Line': 'Línea',
            'Body': 'Carroceria',
            'Color': 'Color',
            'Docment': 'Documento',
        }

class Docments_form(forms.ModelForm):
    Front_photo = forms.ImageField()
    Side_photo = forms.ImageField()
    
    class Meta:
        model = Docments
        fields = [
            'Diving_license',
            'Registration',
            'Gas_sistem_inspection',
            'SOAT',
            'Validity_SOAT',
            'Tecno_mechanical',
            'Operatin_card',
            'Operator',
            'Vehicle_insurance',
            'Policy_number',
            'Vality_Inssurance',
            'Front_photo',
            'Side_photo',
        ]
        labels = {
            'Diving_license': 'Licencia de trancito',
            'Registration': 'Registro',
            'Gas_sistem_inspection': 'Inspección del sistema de gas',
            'SOAT': 'SOAT',
            'Validity_SOAT': 'Vigencia SOAT',
            'Tecno_mechanical': 'Tecno-mecánica',
            'Operatin_card': 'Tarjeta de operación',
            'Operator': 'Operador',
            'Vehicle_insurance': 'Seguro del vehículo',
            'Policy_number': 'Número de póliza',
            'Vality_Inssurance': 'Vigencia del seguro',
            'Front_photo': 'Foto frontal',
            'Side_photo': 'Foto lateral',
        }
        
        widgets = {
            'Validity_SOAT': forms.DateInput(attrs={'type': 'date'}),
            'Tecno_mechanical': forms.DateInput(attrs={'type': 'date'}),
            'Vality_Inssurance': forms.DateInput(attrs={'type': 'date'}),   
            'Front_photo': forms.ClearableFileInput(attrs={
                'capture': 'camera',
            }),
            'Side_photo': forms.ClearableFileInput(attrs={
                'capture': 'camera',
            }),
        }
    
class Tecnical_specifications_form(forms.ModelForm):
    CHOISES_YN= [
                ('Si', 'Si'),
                ('No', 'No'),
                ]
    
    Air_conditioning = forms.ChoiceField(choices=CHOISES_YN, label= 'Aire acondicionado')
    Third_brake_light = forms.ChoiceField(choices=CHOISES_YN, label= 'Tercera luz de freno')
    Side_steps = forms.ChoiceField(choices=CHOISES_YN, label= 'Estribos laterales')
    Airbag = forms.ChoiceField(choices=CHOISES_YN, label= 'Airbag')
    Fog_lights = forms.ChoiceField(choices=CHOISES_YN, label= 'Luces exploradoras')
    Central_locking = forms.ChoiceField(choices=CHOISES_YN, label= 'Bloqueo central')
    Seat_covers = forms.ChoiceField(choices=CHOISES_YN, label= 'Forros de asientos')
    Radio = forms.ChoiceField(choices=CHOISES_YN, label= 'Radio')
    
    class Meta:
        model = Tecnical_specifications
        fields = [
            'Fuel',
            'Drivetrain',
            'Displacement',
            'Drive_type',
            'Tires',
            'Load_capacity',
            'Air_conditioning',
            'Anti_lock_Braking_system',
            'Electronic_Brake_Distribution',
            'Brake_assist',
            'Third_brake_light',
            'Side_steps',
            'Airbag',
            'Fog_lights',
            'Central_locking',
            'Seat_covers',
            'Radio',
            'Power_windows',
            'General_observatios',
        ]
        
        labels = {
            'Fuel': 'Combustible',
            'Drivetrain': 'Sistema de traccion',
            'Displacement': 'Cilindraje (C.C)',
            'Drive_type': 'Tipo de tracción',
            'Tires': 'Llantas',
            'Load_capacity': 'Capacidad de carga',
            'Anti_lock_Braking_system': 'Sistema de frenos antibloqueo',
            'Electronic_Brake_Distribution': 'Distribución electrónica de frenado',
            'Brake_assist': 'Asistencia de frenado',
            'Power_windows': 'Vidrios eléctricos',
            'General_observatios': 'Observaciones generales',
        }
        
        widgets = {
            'General_observatios': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }