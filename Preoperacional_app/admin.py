from django.contrib import admin
from .models import Vehiculo, Datos_generales, Inspeccion
# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(Datos_generales)
admin.site.register(Inspeccion)
