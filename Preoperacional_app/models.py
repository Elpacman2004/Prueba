from django.db import models
from django.utils import timezone
from Hoja_de_vida_vehiculo.models import General_data   
    
class File_History(models.Model):
    Vehicle = models.ForeignKey(General_data, on_delete=models.CASCADE)
    File_path = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File to vehicle {self.Vehicle} created at {self.created_at}"

class Datos_generales(models.Model):
    vehiculo = models.ForeignKey(General_data, on_delete=models.CASCADE)
    Fecha = models.DateField(default=timezone.now)
    Proyecto = models.CharField(default='PP-000-0000', max_length=18,)
    Nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"Datos de la porsona encargada - Nombre de el encargado {self.Nombre}"

class Inspeccion(models.Model):
    fecha = models.DateField(default=timezone.now)

    Nivel_aceite = models.CharField(max_length=250, null=False, blank=False)

    capot_asegurado = models.CharField(max_length=250, null=False, blank=False)
    
    bornes_baterias_ajustados = models.CharField(max_length=250, null=False, blank=False)
    
    indicadores_tablero_control = models.CharField(max_length=250, null=False, blank=False)
    
    kilometraje_inicial = models.IntegerField(default=0, null=False, blank=False)   
    
    aire_acondicionado = models.CharField(max_length=250, null=False, blank=False)
    
    freno_estacionamiento = models.CharField(max_length=250, null=False, blank=False)
    
    limpiaparabrisas = models.CharField(max_length=250, null=False, blank=False)
    
    pito_electrico = models.CharField(max_length=250, null=False, blank=False)
    
    cinturones_seguridad = models.CharField(max_length=250, null=False, blank=False)
    
    equipo_prevencion_seguridad = models.CharField(max_length=250, null=False, blank=False)
    
    botiquin_primeros_auxilios = models.CharField(max_length=250, null=False, blank=False)
    
    extintor = models.CharField(max_length=250, null=False, blank=False)
    
    kit_carreteras = models.CharField(max_length=250, null=False, blank=False)
    
    sensor_externo_velocidad = models.CharField(max_length=250, null=False, blank=False)

    Nivel_del_combustible = models.ImageField(default = False, upload_to='Nivel gasometro', null=False)
    def __str__(self):
        return f"Inspeccion de la fecha {self.fecha}"

class Images(models.Model):
    Nivel_aceite_NC = models.ImageField(default=False, upload_to='Nivel de aceite')
    capot_asegurado_NC = models.ImageField(default=False, upload_to='Capot asegurado')
    bornes_baterias_ajustados_NC = models.ImageField(default=False, upload_to='Bornes baterias ajustados')
    indicadores_tablero_control_NC = models.ImageField(default=False, upload_to='Indicadores tablero control')
    aire_acondicionado_NC = models.ImageField(default=False, upload_to='Aire acondicionado')
    freno_estacionamiento_NC = models.ImageField(default=False, upload_to='Freno estacionamiento')
    limpiaparabrisas_NC = models.ImageField(default=False, upload_to='Limpiaparabrisas')
    pito_electrico_NC = models.ImageField(default=False, upload_to='Pito electrico')
    cinturones_seguridad_NC = models.ImageField(default=False, upload_to='Cinturones seguridad')
    equipo_prevencion_seguridad_NC = models.ImageField(default=False, upload_to='Equipo prevencion seguridad')
    botiquin_primeros_auxilios_NC = models.ImageField(default=False, upload_to='Botiquin primeros auxilios')
    extintor_NC = models.ImageField(default=False, upload_to='Extintor')
    kit_carreteras_NC = models.ImageField(default=False, upload_to='Kit carreteras')
    sensor_externo_velocidad_NC = models.ImageField(default=False, upload_to='Sensor externo velocidad')
    
    funcionamiento_luces_delanteras_NC = models.ImageField(default=False, upload_to='funcionamiento de luces delanteras')
    vidrio_delantero_sin_fisuras_NC = models.ImageField(default=False, upload_to='vidrio delantero sin fisuras')
    placa_delantera_legible_NC = models.ImageField(default=False, upload_to='placa delantera legible')
    Labrado_de_las_llantas_delanteras_NC = models.ImageField(default=False, upload_to='Labrado de las llantas delanteras')
    
    carroceria_buen_estado_NC = models.ImageField(default=False, upload_to='carroceria en buen estado')
    vidrios_laterales_sin_fisuras_NC = models.ImageField(default=False, upload_to='vidrios laterales sin fisuras')
    direccionales_funcionando_NC = models.ImageField(default=False, upload_to='direccionales funcionando')
    espejo_exterior_buen_estado_NC = models.ImageField(default=False, upload_to='espejo exterior buen estado')
    sin_fugas_tanque_combustible = models.ImageField(default=False, upload_to='sin fugas tanque combustible')
    
    luces_traseras_funcionando_NC = models.ImageField(default=False, upload_to='luces traseras funcionando')
    sonido_alarma_reversa_NC = models.ImageField(default=False, upload_to='sonido alarma reversa')
    labrado_llantas_traseras_NC = models.ImageField(default=False, upload_to='labrado de las llantas traseras')
    labrado_llanta_repuesto_NC = models.ImageField(default=False, upload_to='labrado de la llanta repuesto')
    placa_trasera_legible_NC = models.ImageField(default=False, upload_to='placa trasera legible')

class FrontPart (models.Model):
    funcionamiento_luces_delanteras = models.CharField(max_length=250, null=False, blank=False)
    vidrio_delantero_sin_fisuras = models.CharField(max_length=250, null=False, blank=False)
    placa_delantera_legible = models.CharField(max_length=250, null=False, blank=False)
    Labrado_de_las_llantas_delanteras = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return "Parte Delantera"
    
class Side(models.Model):
    carroceria_buen_estado = models.CharField(max_length=250, null=False, blank=False)
    vidrios_laterales_sin_fisuras = models.CharField(max_length=250, null=False, blank=False)
    direccionales_funcionando = models.CharField(max_length=250, null=False, blank=False)
    espejo_exterior_buen_estado = models.CharField(max_length=250, null=False, blank=False)
    sin_fugas_tanque_combustible = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self):
        return "Parte del Costado"
    
class BackPart(models.Model):
    luces_traseras_funcionando = models.CharField(max_length=250, null=False, blank=False)
    sonido_alarma_reversa = models.CharField(max_length=250, null=False, blank=False)
    labrado_llantas_traseras = models.CharField(max_length=250, null=False, blank=False)
    labrado_llanta_repuesto = models.CharField(max_length=250, null=False, blank=False)
    placa_trasera_legible = models.CharField(max_length=250, null=False, blank=False)
    Obser= models.TextField(null=True, blank=True)
    
    def __str__(self):
        return "Parte Trasera"