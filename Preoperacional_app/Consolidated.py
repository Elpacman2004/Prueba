from openpyxl import load_workbook
from openpyxl.styles import Border, Side

thin_border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

def Write_consolidated(GenralData, nombre_archivo):
    wb = load_workbook(filename= 'Z:/SERVER/Dagelec/Logistica/1- VEHICULOS DAGELEC/16. PREOPERACIONALES/1 CONSOLIDADO/Consolidado.xlsx')
    sheet = wb['Consolidado']   
    Initial_Row = 2
    while Initial_Row != 1:
        if sheet['A' + str(Initial_Row)].value == None:
            sheet['A' + str(Initial_Row)] = GenralData['Fecha']
            sheet['A' + str(Initial_Row)].border = thin_border
            sheet['B' + str(Initial_Row)] = GenralData['Proyecto']
            sheet['B' + str(Initial_Row)].border = thin_border
            sheet['C' + str(Initial_Row)] = GenralData['Nombre']
            sheet['C' + str(Initial_Row)].border = thin_border
            sheet['D' + str(Initial_Row)] = str(GenralData['vehiculo'])
            sheet['D' + str(Initial_Row)].border = thin_border
            sheet['E' + str(Initial_Row)] = GenralData['Origen']
            sheet['E' + str(Initial_Row)].border = thin_border
            sheet['F' + str(Initial_Row)] = GenralData['Destino']
            sheet['F' + str(Initial_Row)].border = thin_border
            sheet['G' + str(Initial_Row)] = nombre_archivo
            sheet['G' + str(Initial_Row)].border = thin_border
            wb.save('Z:/SERVER/Dagelec/Logistica/1- VEHICULOS DAGELEC/16. PREOPERACIONALES/1 CONSOLIDADO/Consolidado.xlsx')
            break
        else:
            Initial_Row += 1