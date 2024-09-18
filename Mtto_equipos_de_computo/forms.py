from django import forms
from .models import ComputerEquipmentMaintenance

class ComputerEquipmentMaintenanceForm(forms.ModelForm):

    Choises = [
        ('Cumple', 'Cumple'),
        ('No cumple', 'No cumple'),
        ('No aplica', 'No aplica'),
    ]

    Maintenance_type = [
        ('Preventivo', 'Preventivo'),
        ('Correctivo', 'Correctivo'),
    ] 

    Equipment_type = [
        ('Escritorio', 'Escritorio'),
        ('Laptop', 'Laptop')
    ]

    maintenance_type = forms.ChoiceField(choices=Maintenance_type, widget=forms.Select(attrs={'class': 'Select'}), label='Tipo de Mantenimiento')
    equipment_type = forms.ChoiceField(choices=Equipment_type, widget= forms.Select(attrs={'class': 'Select'}), label='Tipo de Equipo')

    visual_inspection = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Inspección visual, golpes y/o abolladuras')
    complete_screws = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Tornillos completos')
    charging_port = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Puerto de carga')
    port_verification = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Verificación de puertos')
    keyboard_check = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Teclado')
    touchpad_check = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Touchpad')
    screen_check = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Pantalla')
    camera_microphone_verification = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Verificación de cámara y micrófono')
    monitors = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Monitores (Si aplica)')
    peripherals = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Periféricos (Teclado y Mouse)')
    battery_check = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Batería')
    charger_check = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Cargador')

    os_verification = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Verificación del sistema operativo')
    antivirus_verification = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Verificación de antivirus')
    hard_drive_status = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Estado del disco duro')
    temp_files_cleanup = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Limpieza de archivos temporales e innecesarios')
    pending_updates = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Actualizaciones pendientes')
    license_verification = forms.ChoiceField(choices=Choises, widget=forms.RadioSelect(attrs={'class' : 'Radios'}), label='Verificación de Licencias')

    class Meta:
        model = ComputerEquipmentMaintenance
        fields = [
            'computer_equipment_id', 
            'inspection_date', 
            'brand', 
            'maintenance_type', 
            'equipment_type',
            'visual_inspection', 
            'complete_screws', 
            'charging_port', 
            'port_verification',
            'keyboard_check', 
            'touchpad_check', 
            'screen_check', 
            'camera_microphone_verification', 
            'monitors',
            'peripherals', 
            'battery_check', 
            'charger_check', 
            'os_verification', 
            'antivirus_verification',
            'hard_drive_status', 
            'temp_files_cleanup', 
            'pending_updates', 
            'license_verification',
            'corrective_maintenance_notes', 
            'general_observations',
            'received_by', 
            'executed_by'
        ]

        labels = {
            'computer_equipment_id': 'ID Equipo de Computo',
            'inspection_date': 'Fecha de Inspección',
            'brand': 'Marca',
            'maintenance_type': 'Tipo de Mantenimiento',
            'equipment_type': 'Tipo de Equipo',
            'visual_inspection': 'Inspección visual, golpes y/o abolladuras',
            'complete_screws': 'Tornillos completos',
            'charging_port': 'Puerto de carga',
            'port_verification': 'Verificación de puertos',
            'keyboard_check': 'Teclado',
            'touchpad_check': 'Touchpad',
            'screen_check': 'Pantalla',
            'camera_microphone_verification': 'Verificación de cámara y micrófono',
            'monitors': 'Monitores (Si aplica)',
            'peripherals': 'Periféricos (Teclado y Mouse)',
            'battery_check': 'Batería',
            'charger_check': 'Cargador',
            'os_verification': 'Verificación del sistema operativo',
            'antivirus_verification': 'Verificación de antivirus',
            'hard_drive_status': 'Estado del disco duro',
            'temp_files_cleanup': 'Limpieza de archivos temporales e innecesarios',
            'pending_updates': 'Actualizaciones pendientes',
            'license_verification': 'Verificación de Licencias',
            'corrective_maintenance_notes': 'Novedades de Mantenimiento Correctivo',
            'general_observations': 'Observaciones Generales',
            'received_by': 'Recibido por',
            'executed_by': 'Ejecutado por',
        }

        widgets = {
            'inspection_date': forms.DateInput(attrs={'type': 'date'}),
            'corrective_maintenance_notes': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'general_observations': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }