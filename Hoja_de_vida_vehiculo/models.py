from django.db import models

class General_data (models.Model):
    License_plate = models.CharField(max_length=7)
    Class = models.CharField(max_length=50)
    Engine_number = models.CharField(max_length=50)
    Chassis_number = models.CharField(max_length=50)
    Brand = models.CharField(max_length=50)
    Model = models.IntegerField()
    Sevice = models.CharField(max_length=50)
    Owner = models.CharField(max_length=50)
    Line = models.CharField(max_length=50)
    Body = models.CharField(max_length=50)
    Color = models.CharField(max_length=50)
    Docment = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.License_plate}"
    
class Docments (models.Model):
    id_License_plate = models.ForeignKey(General_data, on_delete=models.CASCADE)
    Diving_license = models.CharField(max_length=50)
    Registration = models.CharField(max_length=50)
    Gas_sistem_inspection = models.CharField(max_length=50) 
    SOAT = models.CharField(max_length=50)
    Validity_SOAT = models.DateField(null=True, blank=True)
    Tecno_mechanical = models.DateField(null=True, blank=True)
    Operatin_card = models.CharField(max_length=50)
    Operator = models.CharField(max_length=50)
    Vehicle_insurance = models.CharField(max_length=50) 
    Policy_number = models.IntegerField(null=True, blank=True)
    Vality_Inssurance = models.DateField(null=True, blank=True)
    Front_photo = models.ImageField(upload_to='photos_vehicle/')
    Side_photo = models.ImageField(upload_to='photos_vehicle/')
    
class Tecnical_specifications (models.Model):
    id_License_plate = models.ForeignKey(General_data, on_delete=models.CASCADE)
    Fuel = models.CharField(max_length=50)
    Drivetrain = models.CharField(max_length=50)
    
    Displacement = models.IntegerField()
    Drive_type = models.CharField(max_length=50)
    
    Tires = models.CharField(max_length=50)
    Load_capacity = models.CharField(max_length=100)
    
    Air_conditioning = models.CharField(max_length=50)
    Anti_lock_Braking_system = models.CharField(max_length=50)
    Electronic_Brake_Distribution = models.CharField(max_length=50)
    Brake_assist = models.CharField(max_length=50)
    Third_brake_light = models.CharField(max_length=50)
    Side_steps = models.CharField(max_length=50)
    Airbag = models.CharField(max_length=50)
    Fog_lights = models.CharField(max_length=50)
    Central_locking = models.CharField(max_length=50)
    Seat_covers = models.CharField(max_length=50)
    Radio = models.CharField(max_length=50)
    Power_windows = models.CharField(max_length=50)
    General_observatios = models.TextField(null=True, blank=True)