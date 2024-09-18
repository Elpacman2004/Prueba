from django.db import models

class EquipmentInspection(models.Model):
    place = models.CharField(max_length=50)
    id_eqipment = models.CharField(max_length=50)
    date = models.DateField()
    brand = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)
    visual_check = models.CharField(max_length=50)
    loose_fasteners = models.CharField(max_length=50)
    power_connections_ok = models.CharField(max_length=50)
    power_button_ok = models.CharField(max_length=50)
    fuses_ok = models.CharField(max_length=50)
    power_cable_ok = models.CharField(max_length=50)
    noises = models.CharField(max_length=50)
    loose_parts = models.CharField(max_length=50)
    temp_humidity = models.CharField(max_length=50)
    display_ok = models.CharField(max_length=50)
    other_components_ok = models.CharField(max_length=50)
    current_cable = models.CharField(max_length=50)
    voltage_cables = models.CharField(max_length=50)
    measurement_cables = models.CharField(max_length=50)
    ac_voltage_outputs = models.CharField(max_length=50)
    dc_current_outputs = models.CharField(max_length=50)
    ac_current_outputs = models.CharField(max_length=50)
    ac_voltage_input = models.CharField(max_length=50)
    dc_voltage_input = models.CharField(max_length=50)
    dc_current_input = models.CharField(max_length=50)
    ac_current_input = models.CharField(max_length=50)
    resistance_measurement = models.CharField(max_length=50)
    notes = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.date}"