from django import forms
from .models import GeneralData, Staff_requisition, Data_of_selected_personnel, Conditions_of_employment, Salary_assignment
from datetime import time

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
        
        widgets = {
            'Date_of_application': forms.DateInput(attrs={'type': 'date'}),
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

class Data_of_selected_personnelForm(forms.ModelForm):
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
        model = Data_of_selected_personnel
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
    
class TimeInput(forms.TimeInput):
    input_type = 'time'
    format = '%H:%M'   
    
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
        fields = ['Hired', 'Type_of_Contract', 'Overtime_Hours', 'Duration_of_Engagement', 'Management_and_Trust', 'Workplace', 'Start_Date', 'Monday_to_Friday_start', 'Monday_to_Friday_end', 'Saturday_start', 'Saturday_end']
        labels = {
            'Hired': 'Contratado',
            'Type_of_Contract': 'Clase de contrato',
            'Overtime_Hours': 'Horas extras',
            'Duration_of_Engagement': 'Tiempo de vinculación:',
            'Management_and_Trust': 'Manejo y confianza',
            'Workplace': 'Lugar de trabajo',
            'Start_Date': 'Fecha Inicio de labores:',
            'Monday_to_Friday_start': 'Hora de entrada dias lunes a viernes',
            'Monday_to_Friday_end': 'Hora de salida dias lunes a viernes',
            'Saturday_start': 'Hora de entrada dia sabado',
            'Saturday_end': 'Hora de salida dia sabado',
        }
        
        widgets = {
            'Duration_of_Engagement': forms.DateInput(attrs={'type': 'date'}),
            'Start_Date': forms.DateInput(attrs={'type': 'date'}),
            'Monday_to_Friday_start': TimeInput(format='%H:%M'),
            'Monday_to_Friday_end': TimeInput(format='%H:%M'),
            'Saturday_start': TimeInput(format='%H:%M'),
            'Saturday_end': TimeInput(format='%H:%M'),
        }
        
class Salary_assignment_form (forms.ModelForm):
    
    Choises_TA = [
        ('Yes', 'Si'),
        ('No', 'No'),
    ]
    Transportation_Allowance = forms.ChoiceField(choices=Choises_TA, widget=forms.RadioSelect, label= 'Subsidio de transporte')
        
    Choises_TVA = [
        ('Yes', 'Si'),
        ('No', 'No'),
    ]
    Travel_Allowance = forms.ChoiceField(choices=Choises_TVA, widget=forms.RadioSelect, label='Viaticos')
    
    Choises_O = [
        ('Yes', 'Si'),
        ('No', 'No'),
    ]
    Other = forms.ChoiceField(choices=Choises_O, widget=forms.RadioSelect, label='Otros')
        
    class Meta:
        model = Salary_assignment
        fields = ['Basic_salary', 'Transportation_Allowance', 'Value_Transportation_Allowance', 'Bonus', 'Travel_Allowance', 'Value_Travel_Allowance', 'Other', 'Which', 'Observations']
        labels = {
            'Basic_salary': 'Salario basico',
            'Value_Transportation_Allowance': 'Valor del subsidio de transporte',
            'Bonus': 'Bonificacion',
            'Value_Travel_Allowance': 'Valor de los viaticos',
            'Which': 'Cual',
            'Observations': 'Observaciones'
        }