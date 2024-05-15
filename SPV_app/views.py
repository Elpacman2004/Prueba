from django.shortcuts import render, redirect
from .froms import GeneralDataForm, Staff_requisitionForm, Human_ResourcesForm, Conditions_of_employmentForm
import os
import shutil
from openpyxl import Workbook, load_workbook

def IndexSPV (request):
    return render(request, 'IndexSPV.html')

def GeneralForm_SPV (request):
    if request.method == 'POST':
        form = GeneralDataForm(request.POST)
        if form.is_valid():
            Clean_data = form.cleaned_data
            print(Clean_data)
            New_file =  f'C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/SPV/{Clean_data["Name"]} SPV.xlsx'
            request.session['file name'] = New_file
            
            shutil.copy('C:/Users/Dagelec LTDA/Desktop/Pruebas_excel/PlantillaSPV.xlsx', New_file)
            
            wb = load_workbook(filename= New_file)
            
            sheet = wb['F-S4-01 Rev 03']
            sheet['B7'] = Clean_data['City']
            sheet['B8'] = Clean_data['Name']
            sheet['B9'] = Clean_data['Process_Project']
            sheet['N7'] = Clean_data['Date_of_application']
            sheet['N8'] = Clean_data['Applicants_Position']
            
            wb.save(New_file)
            form.save()
            return redirect ('Staff requisition')
        
    else:
        error = request.session.get('error', None)
        print (error)
        form = GeneralDataForm()
        return render(request, 'Forms/GeneralForm.html', {
                                                        'form': form,
                                                        'error': error,
                                                          })
    
def Staff_requisition (request):
    if request.method == 'POST':
        form = Staff_requisitionForm(request.POST)
        if form.is_valid():
            file_name = request.session.get('file name', None)
            
            Clean_data = form.cleaned_data
            print(file_name)
            print(Clean_data)
            
            
            wb = load_workbook(filename= file_name)
            sheet = wb['F-S4-01 Rev 03']
            if Clean_data['Reason'] == 'New_Position':
                sheet['C13'] = 'X'
            elif Clean_data['Reason'] == 'Temporary':
                sheet['E13'] = 'X'
            elif Clean_data['Reason'] == 'New_Project':
                sheet['G13'] = 'X'  
            elif Clean_data['Reason'] == 'Other':
                sheet['I13'] = 'X'
            else:
                print ('Error value is not valid')
            
            if Clean_data['Which'] == None:
                sheet['L13'] = ''
            else:
                sheet['L13'] = Clean_data['Which']
            
            sheet['B14'] = Clean_data['Name_of_the_Position_Requested']
            sheet['B15'] = Clean_data['Job_Profile']
                
            wb.save(file_name)
            
            return redirect ('Human Resources')
        
        else:
            print(form.errors)
            return render(request, 'Forms/Staff requisition form.html', {'form': form})
            
    else:
        form = Staff_requisitionForm()
        return render(request, 'Forms/Staff requisition form.html', {'form': form})
    
def Human_Resources (request):
        if request.method == 'POST':
            form = Human_ResourcesForm(request.POST)
            if form.is_valid():
                Name = request.session.get('file name')
                if Name is None:
                    request.session['error'] = 'Deves llenar el formulario General SPV primero'         
                    return redirect ('General SPV') 
                
                
                Clean_data = form.cleaned_data
                print(Clean_data)
                
                wb = load_workbook(filename= Name)
                sheet = wb['F-S4-01 Rev 03']
            
                sheet['B20'] = Clean_data['Name'] 
                sheet['K20'] = Clean_data['Identification_document']
                sheet['B21'] = Clean_data['Adress']
                if Clean_data['Phone_number'] == 'None':
                    pass
                else:
                    sheet['B22'] = Clean_data['Phone_number']
                sheet['N21'] = Clean_data['Movile_number']
                sheet['B22'] = Clean_data['Current_HIP']
                sheet['G22'] = Clean_data['AFP']
                sheet['L22'] = Clean_data['RH']
                if Clean_data['Phone_number'] == 'None':
                        pass
                else:
                    sheet['B23'] = Clean_data['Phone_number']
                if Clean_data['Yellow_fever'] == 'Yes':
                    sheet['K23'] = 'X'
                else:
                    sheet['M23'] = 'X'
                if Clean_data['Tetanus'] == 'Yes':
                    sheet['R23'] = 'X'
                else:
                    sheet['T23'] = 'X'
                if Clean_data['Medical_examination'] == 'Yes':
                    sheet['C25'] = 'X'
                else:
                    sheet['E25'] = 'X'
                if Clean_data['Does_the_applicant_meet_the_job_profile'] == 'Yes':
                    sheet['N25'] = 'X'
                elif Clean_data['Does_the_applicant_meet_the_job_profile'] == 'No':
                    sheet['P25'] = 'X'
                else:
                    sheet['T25'] = 'X'
                sheet['B26'] = Clean_data['Pants']
                sheet['G26'] = Clean_data['Shirt']  
                sheet['K26'] = Clean_data['Shoes']
                sheet['R26'] = Clean_data['Overall']
                if Clean_data['Phone_number'] == 'None':
                    pass
                else:
                    sheet['B27'] = Clean_data['Observations']
                if Clean_data['Phone_number'] == 'None':
                    pass
                else:
                    sheet['B29'] = Clean_data['Work_References']
                sheet['B33'] = Clean_data['Personal_References']
                
                wb.save(Name)
                
                return redirect ('IndexSPV')
        else:
            form = Human_ResourcesForm()
            return render(request, 'Forms/Human_Resources.html', {'form': form})
        
def Conditions_of_employment (request):
    if request.method == 'POST':
        form = Conditions_of_employmentForm(request.POST)
        if form.is_valid():
            Clean_data = form.cleaned_data
            print(Clean_data)
            form.save()
            return redirect ('IndexSPV')       