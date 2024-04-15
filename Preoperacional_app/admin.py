from django.contrib import admin
from .models import Vehiculo, Datos_generales, Inspeccion, ParteDelantera, Costado, ParteTrasera
# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(Datos_generales)
admin.site.register(Inspeccion)
admin.site.register(ParteDelantera)
admin.site.register(Costado)
admin.site.register(ParteTrasera)