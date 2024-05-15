from django import forms
from .models import GeneralData, Staff_requisition, Human_Resources, Conditions_of_employment

class GeneralDataForm(forms.ModelForm):
    class Meta:
        model = GeneralData
        fields = ['City', 'Name', 'Process_Project', 'Date_of_application', 'Applicants_Position']
        labels = {
            'City': 'Ciudad',
            'Name': 'Nombre del solicitante',
            'Process_Project': 'Proceso/Proyecto',
            'Date_of_application': 'Fecha de solicitud',
            'Applicants_Position': 'Cargo del solicitante',
        }

class Staff_requisitionForm(forms.ModelForm):
    CHOICES = [
        ('New_Position', 'Nuevo cargo'),
        ('Temporary', 'Temporal'),
        ('New_Project', 'Nuevo proyecto'),
        ('Other', 'Otro'),
    ]
    
    Reason = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Staff_requisition
        fields = ['Reason', 'Which', 'Name_of_the_Position_Requested', 'Job_Profile']
        labels = {
            'Reason': 'Razon',
            'Which': '¿Cual?',
            'Name_of_the_Position_Requested': 'Nombre del cargo solicitado',
            'Job_Profile': 'Perfil del cargo',
        }

class Human_ResourcesForm(forms.ModelForm):
    choises_YF = [
        ('Yes', 'Si'),
        ('No', 'No'),
    ]
    Yellow_fever = forms.ChoiceField(choices=choises_YF, widget=forms.RadioSelect, label='Fiebre amarilla')
    
    choises_T = [
        ('Yes', 'Si'),
        ('No', 'No'),
    ]
    Tetanus = forms.ChoiceField(choices=choises_T, widget=forms.RadioSelect, label='Tetano')    
    
    choises_ME = [
        ('Yes', 'Aprobado'),
        ('No', 'Rechazado'),
    ]
    Medical_examination = forms.ChoiceField(choices=choises_ME, widget=forms.RadioSelect, label='Examen medico')
    
    choises_J = [
        ('Yes', 'Si'),
        ('No', 'No'),
        ('N/A', 'No aplica')
    ]
    Does_the_applicant_meet_the_job_profile = forms.ChoiceField(choices=choises_J, widget=forms.RadioSelect, label='¿Cumple el perfil del cargo?')
    
    choises_Shirt = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),  
    ]
    Shirt = forms.ChoiceField(choices=choises_Shirt, label='Camisa')
    
    chises_Overall = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),   
    ]
    Overall = forms.ChoiceField(choices=chises_Overall, label='Overol')
    
    class Meta:
        model = Human_Resources
        fields = ['Name', 'Identification_document', 'Adress', 'Phone_number', 'Movile_number', 'Current_HIP', 'AFP', 'RH', 'Allergies', 'Yellow_fever', 'Tetanus', 'Medical_examination', 'Does_the_applicant_meet_the_job_profile', 'Pants', 'Shirt', 'Shoes', 'Overall', 'Observations', 'Work_References', 'Personal_References']
        labels = {
            'Name': 'Nombre',
            'Identification_document': 'Documento de identificacion',
            'Adress': 'Direccion',
            'Phone_number': 'Telefono',
            'Movile_number': 'Celular',
            'Current_HIP': 'EPS actual',
            'AFP': 'AFP',
            'RH': 'RH',
            'Allergies': 'Alergias',
            'Pants': 'Pantalones',
            'Shoes': 'Zapatos',
            'Observations': 'Observaciones',
            'Work_References': 'Referencias laborales',
            'Personal_References': 'Referencias personales',
        }
        
class Conditions_of_employmentForm(forms.ModelForm):
    Choises_H = [
        ('Yes', 'Si'),
        ('No', 'No'),
    ]
    Hired = forms.ChoiceField(choices=Choises_H, widget=forms.RadioSelect, label='Contratado')
    
    Choises_OH = [
        ('Yes', 'Si'),
        ('No', 'No'),
    ]
    Overtime_Hours = forms.ChoiceField(choices=Choises_OH, widget=forms.RadioSelect, label='Horas extras')
    
    Choises_MT = [
        ('Yes', 'Si'),
        ('No', 'No'),
    ]
    Management_and_Trust = forms.ChoiceField(choices=Choises_MT, widget=forms.RadioSelect, label='Manejo y confianza')  
    
    
    
    class Meta:
        model = Conditions_of_employment
        fields = ['Hired', 'Type_of_Contract', 'Overtime_Hours', 'Duration_of_Engagement', 'Management_and_Trust', 'Workplace', 'Start_Date', 'Monday_to_Friday_start', 'Saturday_start']
        labels = {
            'Hired': 'Contratado',
            'Type_of_Contract': 'Tipo de contrato',
            'Overtime_Hours': 'Horas extras',
            'Duration_of_Engagement': 'Tiempo de vinculación:',
            'Management_and_Trust': 'Manejo y confianza',
            'Workplace': 'Lugar de trabajo',
            'Start_Date': 'Fecha Inicio de labores:',
            'Monday_to_Friday_start': 'Lunes a viernes',
            'Saturday_start': 'Sabado',   
        }