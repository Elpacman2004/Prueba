from django.db import models
from django.utils import timezone

class Vehiculo(models.Model):
    Placa = models.CharField(max_length=20)

    def __str__(self):
        return f"Datos del vehículo - Vehículo {self.Placa}"

class Datos_generales(models.Model):
    Fecha = models.DateField(default=timezone.now)
    Proyecto = models.CharField(default='PP-proyecto-año', max_length=18,)
    Nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"Datos de la porsona encargada - Nombre de el encargado {self.Nombre}"

class Inspeccion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)

    fecha = models.DateField(default=timezone.now)

    Nivel_aceite = models.CharField(max_length=250, null=False, blank=False)
    Nivel_aceite_NC = models.ImageField(default=False, upload_to='Nivel de aceite')

    capot_asegurado = models.CharField(max_length=250, null=False, blank=False)
    capot_asegurado_NC = models.ImageField(default=False, upload_to='Capot_asegurado')


    kilometraje_inicial = models.IntegerField(default=0, null=False)
    Nivel_gasometro = models.ImageField(default = False, upload_to='Nivel gasometro', null=False)

    def __str__(self):
        return f"Inspeccion de {self.vehiculo} el {self.fecha}"

