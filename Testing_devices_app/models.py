from django.db import models
from django.utils import timezone

class GeneralDataDV(models.Model):
    NameD = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100)
    Acquisition_Date = models.DateField()
    Supply_Voltage = models.CharField(max_length=100)
    RefModel = models.CharField(max_length=100)
    Supplier = models.CharField(max_length=100)
    Serial_number = models.CharField(max_length=100)
    Invoice = models.CharField(max_length=100)
    Type_device = models.CharField(max_length=100)
    
    def __str__(self):
        return self.NameD
    
class DFAD(models.Model):
    Equipment_description = models.TextField() 
    Photograph = models.ImageField(upload_to='Fotos de dispositivos')
    Observations = models.TextField(blank=True, null=True)
    
    
    
    
class IMC (models.Model):
    Device = models.ForeignKey(GeneralDataDV, on_delete=models.CASCADE)
    Date = models.DateField(default=timezone.now)
    Activity_description = models.CharField(max_length=100)
    Activity_type = models.CharField(max_length=100)    
    Certificate_docment_number = models.CharField(max_length=100)
    Satisfactory_result = models.CharField(max_length=100)
    Action_to_take = models.CharField(max_length=100)
    Next_revew = models.DateField()
    Frequency = models.CharField(max_length=100)
    Responsible = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.NameD