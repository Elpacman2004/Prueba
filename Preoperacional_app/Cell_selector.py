from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
import pandas as pd
from openpyxl.styles import Border, Side
import base64
from openpyxl.drawing.image import Image
from django.core.files.base import ContentFile
import io
from PIL import Image as PILImage

thin_border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

def process_form(dia_semana, form, sheet, N):
    print(dia_semana)
    campos_ignorar = ['First_Aid_Kit_LI', 'Fire_Extinguisher_ED', 'Spill_Kit_LI']
    day_to_column = {
        'Lunes': 'G',
        'Martes': 'H',
        'Miercoles': 'I',
        'Jueves': 'J',
        'Viernes': 'K',
        'Sábado': 'L',
        'Domingo': 'M'
    }
    column = day_to_column[dia_semana]
    print('Columna:', column)

    for field, value in form.cleaned_data.items():
        if field in campos_ignorar:
            continue
        else:
            if N > 41:  
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
        'Miercoles': 'I',
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
    sheet[column+'45'] =  General_Data['Fecha']

def Signatures(hoy_y_hora, General_Data, request, sheetF):
    Firma = request.POST['firmaData']	
    format, imgstr = Firma.split(';base64,')
    ext = format.split('/')[-1]
    data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

    # Guarda los datos en un BytesIO para poder leerlos varias veces
    data_io = io.BytesIO(data.read())

    image = PILImage.open(data_io)

    if image.getbbox():
        with open(f'signature.png', 'wb') as f:
            # Retrocede el puntero del BytesIO al principio
            data_io.seek(0)
            f.write(data_io.read())

            # Retrocede el puntero del BytesIO al principio
            data_io.seek(0)
            img = PILImage.open(data_io)

            # Cambia el tamaño de la imagen
            img = img.resize((130, 50))

            # Guarda la imagen en un archivo
            img.save(f'signature.png')

            # Cargar la imagen usando openpyxl
            signature_img = Image('signature.png')

    col = 'A'
    while True:
        for row in range(1, 27, 5):  
                cell1 = sheetF[f'{col}{row}']
                cell2 = sheetF[f'{col}{row + 1}']
                cell3 = sheetF[f'{col}{row + 2}']
                cell4 = sheetF[f'{col}{row + 3}']
                cell5 = sheetF[f'{col}{row + 4}']
                if cell1.value is None and cell4.value is None and cell5.value is None and row <= 25:
                    cell1.value = hoy_y_hora
                    cell1.border = thin_border
                    cell2.value = General_Data['Origen']
                    cell2.border = thin_border
                    cell3.value = General_Data['Destino']
                    cell3.border = thin_border
                    cell4.value = General_Data['Nombre']
                    cell4.border = thin_border
                    signature_img.anchor = f'{col}{row + 4}'
                    sheetF.add_image(signature_img)
                    cell5.border = thin_border
                    break
                else:
                    pass

                if row >= 25:
                    col = chr(ord(col) + 1)
        else:
            continue
        break


def write_message_to_sheet(differences, df_O, sheet, N, dia_semana, hoy):
    for index, row in differences.iterrows():
        for column in differences.columns:
            if column[1] == 'self' and pd.notna(row[column]):
                previous_value = row[(column[0], "self")]
                new_value = row[(column[0], "other")]

                if previous_value == 'None':
                    dia_semana = ''
                else:
                    message = (f'En el campo {df_O.loc[index, 0]} fue cambiado de {previous_value} a {new_value}.')

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
                print(message)

                if column:
                    Loop_break = False
                    while Loop_break != True:
                        existing_value = sheet[column+str(N)].value
                        if existing_value is not None:
                            N = N + 1
                        else:
                            sheet[column+str(N)] = message
                            N = N + 1
                            Loop_break = True
                else:
                    dia_semana = dia_semana[hoy.weekday()]
    return N

def week_of_month(dt):
    Monday = {0:1, 7:2, 14:3, 21:4, 28:5}
    Tuesday = {0:1, 6:2, 13:3, 20:4, 27:5}
    Wednesday = {0:1, 5:2, 12:3, 19:4, 26:5}
    Thursday = {0:1, 4:2, 11:3, 18:4, 25:5}
    Friday = {0:1, 3:2, 10:3, 17:4, 24:5}
    Saturday = {2:2, 9:3, 16:4, 23:5}
    Sunday = {0:1, 1:2, 8:3, 15:4, 22:5, 29:6}


    Now = dt
    Current_day = Now.day

    First_day_month = Now.replace(day=1)
    First_day_name = First_day_month.strftime("%A")

    if First_day_name == "Monday":
        selected_dict = Monday
    elif First_day_name == "Tuesday":
        selected_dict = Tuesday
    elif First_day_name == "Wednesday":
        selected_dict = Wednesday
    elif First_day_name == "Thursday":
        selected_dict = Thursday
    elif First_day_name == "Friday":
        selected_dict = Friday
    elif First_day_name == "Saturday":
        selected_dict = Saturday
    elif First_day_name == "Sunday":
        selected_dict = Sunday
    else:
        selected_dict = {}

        
    for key in sorted(selected_dict.keys(), reverse=True):
        if Current_day > key:
            Current_wek = selected_dict[key]
            break
        else:
            continue

    return Current_wek