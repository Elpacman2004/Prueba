from django.db import models

class ComputerEquipmentMaintenance(models.Model):
    computer_equipment_id = models.CharField(default='COM-', max_length=100)
    inspection_date = models.DateField()
    brand = models.CharField(max_length=100)
    maintenance_type = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=100)
    visual_inspection = models.CharField(max_length=50)
    complete_screws = models.CharField(max_length=50)
    charging_port = models.CharField(max_length=50)
    port_verification = models.CharField(max_length=50)
    keyboard_check = models.CharField(max_length=50)
    touchpad_check = models.CharField(max_length=50)
    screen_check = models.CharField(max_length=50)
    camera_microphone_verification = models.CharField(max_length=50)
    monitors = models.CharField(max_length=50, null=True, blank=True)
    peripherals = models.CharField(max_length=50, null=True, blank=True) 
    battery_check = models.CharField(max_length=50)
    charger_check = models.CharField(max_length=50)
    os_verification = models.CharField(max_length=50)
    antivirus_verification = models.CharField(max_length=50)
    hard_drive_status = models.CharField(max_length=100)
    temp_files_cleanup = models.CharField(max_length=50)
    pending_updates = models.CharField(max_length=50)
    license_verification = models.CharField(max_length=50)  
    corrective_maintenance_notes = models.TextField(null=True, blank=True)
    general_observations = models.TextField(null=True, blank=True)
    received_by = models.CharField(max_length=100)
    executed_by = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.computer_equipment_id} - {self.inspection_date}"
