from django.db import models
from django.utils import timezone
from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import time

class GeneralData(models.Model):
    City = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Process_Project = models.CharField(max_length=100)
    Date_of_application = models.DateField(default= timezone.now)
    Applicants_Position = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
    
class Staff_requisition (models.Model):
    Reason = models.CharField(max_length=100)
    Which = models.CharField(max_length=250, blank=True, null=True)
    Name_of_the_Position_Requested = models.CharField(max_length=100)
    Job_Profile = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name_of_the_Position_Requested
    
class Human_Resources (models.Model):
    Name = models.CharField(max_length=100)
    Identification_document = models.IntegerField()
    Adress = models.CharField(max_length=100)
    Phone_number = models.IntegerField(null=True, blank=True)
    Movile_number = models.IntegerField()
    Current_HIP = models.CharField(max_length=100)
    AFP = models.CharField(max_length=100)
    RH = models.CharField(max_length = 3)
    Allergies = models.CharField(max_length=100, null=True, blank=True)
    Yellow_fever = models.CharField(max_length=100)
    Tetanus = models.CharField(max_length=100)
    Medical_examination = models.CharField(max_length=100)
    Does_the_applicant_meet_the_job_profile = models.CharField(max_length=100)
    Pants = models.IntegerField()
    Shirt = models.CharField(max_length= 2)
    Shoes = models.IntegerField()
    Overall = models.CharField(max_length= 2)
    Observations = models.TextField(null=True, blank=True)
    Work_References = models.TextField(null=True, blank=True)
    Personal_References = models.TextField(null=False, blank=False) 
    
    def __str__(self):
        return self.Name
    
class Conditions_of_employment (models.Model):
    Hired = models.CharField(max_length=2)
    Type_of_Contract = models.CharField(max_length=100)
    Overtime_Hours = models.CharField(max_length=2)
    Duration_of_Engagement = models.DateField(default=date.today() + relativedelta(years=1))
    Management_and_Trust = models.CharField(max_length=2)
    Workplace = models.CharField(max_length=100)
    Start_Date = models.DateField(default= timezone.now)
    Monday_to_Friday_start = models.TimeField(default=time(7, 0))
    Monday_to_Friday_end = models.TimeField(default=time(17, 0))
    Saturday_start = models.TimeField(default=time(7, 0))
    Saturday_end = models.TimeField(default=time(17, 0))
    
    def __str__(self):
        return self.Name