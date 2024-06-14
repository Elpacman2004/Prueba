from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
import pandas as pd


def process_form(dia_semana, form, sheet, N):
    day_to_column = {
        'Lunes': 'G',
        'Martes': 'H',
        'Miércoles': 'I',
        'Jueves': 'J',
        'Viernes': 'K',
        'Sábado': 'L',
        'Domingo': 'M'
    }
    column = day_to_column[dia_semana]

    for field, value in form.cleaned_data.items():
        if N < 41:
            break
        if isinstance(value, InMemoryUploadedFile):
            file_content = value.read()
        elif value in ['C', 'NC', 'NA']:
            if isinstance(value, InMemoryUploadedFile):
                sheet[column+str(N)] = value.name
            elif hasattr(value, 'temporary_file_path'):
                sheet[column+str(N)] = value.temporary_file_path()
            else:
                sheet[column+str(N)] = value
        else:
            if isinstance(value, TemporaryUploadedFile):
                sheet[column+str(N)] = value.temporary_file_path() 
            else:
                sheet[column+str(N)] = value
        N += 1
        


def write_to_sheet(dia_semana, hora, sheet, General_Data):
    day_to_column = {
        'Lunes': 'G',
        'Martes': 'H',
        'Miércoles': 'I',
        'Jueves': 'J',
        'Viernes': 'K',
        'Sábado': 'L',
        'Domingo': 'M'
    }
    column = day_to_column[dia_semana]

    if hora >= 6 and hora < 14:
        sheet[column+'42'] = General_Data['Nombre']
    elif hora >= 14 and hora < 22:
        sheet[column+'43'] = General_Data['Nombre'] 
    else:
        sheet[column+'44'] = General_Data['Nombre']   

    sheet[column+'45'] = General_Data['Fecha']
    


def write_message_to_sheet(differences, df_O, sheet, N, dia_semana, hoy):
    for index, row in differences.iterrows():
        for column in differences.columns:
            if column[1] == 'self' and pd.notna(row[column]):
                previous_value = row[(column[0], "self")]
                new_value = row[(column[0], "other")]

                if previous_value != 'none':
                    message = (f'En el campo {df_O.loc[index, 0]} fue cambiado de {previous_value} a {new_value}.')
                else:
                    dia_semana = ''

                day_to_column = {
                    'Lunes': 'A',
                    'Martes': 'C',
                    'Miercoles': 'E',
                    'Jueves': 'G',
                    'Viernes': 'I',
                    'Sábado': 'K',
                    'Domingo': 'M'
                }
                column = day_to_column.get(dia_semana)

                if column:
                    sheet[column+str(N)] = message
                    N = N + 1
                else:
                    dia_semana = dia_semana[hoy.weekday()]
    return N