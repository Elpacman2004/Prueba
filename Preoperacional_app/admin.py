from django.contrib import admin
from .models import Datos_generales, Inspeccion, FrontPart, Side, BackPart, File_History, Images
from Hoja_de_vida_vehiculo.models import General_data
# Register your models here.

admin.site.register(Datos_generales)
admin.site.register(Inspeccion)
admin.site.register(FrontPart)
admin.site.register(Side)
admin.site.register(BackPart)
admin.site.register(File_History)
admin.site.register(Images)