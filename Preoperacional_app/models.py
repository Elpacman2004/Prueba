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
    
    Nivel_aceite = models.BooleanField(default=False )
    Nivel_aceite_NC = models.ImageField(default=False,upload_to = 'Nivel de aceite')
    Nivel_aceite_NA = models.BooleanField(default=False)
    
    capot_asegurado = models.BooleanField(default=False)
    capot_asegurado_NC = models.ImageField(default=False, upload_to='Capot_asegurado')
    capot_asegurado_NA = models.BooleanField(default=False)
    
    kilometraje_inicial = models.IntegerField(default=0, null=False)
   
    Nivel_gasometro = models.ImageField(default = False, upload_to='Nivel gasometro', null=False)
    
    


    def __str__(self):
        return f"Inspeccion de {self.vehiculo} el {self.fecha}"

class ParteDelantera(models.Model):
    funcionamiento_luces_delanteras = models.BooleanField(default=False)
    vidrio_delantero_sin_fisuras = models.BooleanField(default=False)
    placa_delantera_legible = models.BooleanField(default=False)
    Labrado_de_las_llantas_delanteras = models.BooleanField(default=False)

    funcionamiento_luces_delanteras_NC = models.ImageField(default=False, upload_to='funcionamiento de luces delanteras')
    vidrio_delantero_sin_fisuras_NC = models.ImageField(default=False, upload_to='vidrio delantero sin fisuras')
    placa_delantera_legible_NC = models.ImageField(default=False, upload_to='placa delantera legible')
    Labrado_de_las_llantas_delanteras_NC = models.ImageField(default=False, upload_to='Labrado de las llantas delanteras')
    
    funcionamiento_luces_delanteras_NA = models.BooleanField(default=False)
    vidrio_delantero_sin_fisuras_NA = models.BooleanField(default=False)
    placa_delantera_legible_NA = models.BooleanField(default=False)
    Labrado_de_las_llantas_delanteras_NA = models.BooleanField(default=False)
    
    def __str__(self):
        return "Parte Delantera"

class Costado(models.Model):
    carroceria_buen_estado = models.BooleanField(default=False)
    vidrios_laterales_sin_fisuras = models.BooleanField(default=False)
    direccionales_funcionando = models.BooleanField(default=False)
    espejo_exterior_buen_estado = models.BooleanField(default=False)
    sin_fugas_tanque_combustible = models.BooleanField(default=False)
    
    carroceria_buen_estado_NC = models.ImageField(default=False, upload_to='carroceria en buen estado')
    vidrios_laterales_sin_fisuras_NC = models.ImageField(default=False, upload_to='vidrios laterales sin fisuras')
    direccionales_funcionando_NC = models.ImageField(default=False, upload_to='direccionales funcionando')
    espejo_exterior_buen_estado_NC = models.ImageField(default=False, upload_to='espejo exterior buen estado')
    sin_fugas_tanque_combustible_NC = models.ImageField(default=False, upload_to='sin fugas en el tanque combustible')
    
    carroceria_buen_estado_NA = models.BooleanField(default=False)
    vidrios_laterales_sin_fisuras_NA = models.BooleanField(default=False)
    direccionales_funcionando_NA = models.BooleanField(default=False)
    espejo_exterior_buen_estado_NA = models.BooleanField(default=False)
    sin_fugas_tanque_combustible_NA = models.BooleanField(default=False)

    def __str__(self):
        return "Costado"

class ParteTrasera(models.Model):
    luces_traseras_funcionando = models.BooleanField(default=False)
    sonido_alarma_reversa = models.BooleanField(default=False)
    labrado_llantas_traseras = models.BooleanField(default=False)
    labrado_llanta_repuesto = models.BooleanField(default=False)
    placa_trasera_legible = models.BooleanField(default=False)
    
    luces_traseras_funcionando_NC = models.ImageField(default=False, upload_to='luces traseras funcionando')
    sonido_alarma_reversa_NC = models.ImageField(default=False, upload_to='sonido alarma reversa')
    labrado_llantas_traseras_NC = models.ImageField(default=False, upload_to='labrado de las llantas traseras')
    labrado_llanta_repuesto_NC = models.ImageField(default=False, upload_to='labrado de la llanta repuesto')
    placa_trasera_legible_NC = models.ImageField(default=False, upload_to='placa trasera legible')
    
    luces_traseras_funcionando_NA = models.BooleanField(default=False)
    sonido_alarma_reversa_NA = models.BooleanField(default=False)
    labrado_llantas_traseras_NA = models.BooleanField(default=False)
    labrado_llanta_repuesto_NA = models.BooleanField(default=False)
    placa_trasera_legible_NA = models.BooleanField(default=False)

    def __str__(self):
        return "Parte Trasera"
