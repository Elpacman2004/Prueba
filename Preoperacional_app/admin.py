from django.contrib import admin
from .models import Vehiculo, Datos_generales, Inspeccion, FrontPart, Side, BackPart, Histoial_archivos, Images
# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(Datos_generales)
admin.site.register(Inspeccion)
admin.site.register(FrontPart)
admin.site.register(Side)
admin.site.register(BackPart)
admin.site.register(Histoial_archivos)
admin.site.register(Images)