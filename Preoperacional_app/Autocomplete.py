from dal import autocomplete
from .models import Vehiculo

class VehiculoAutocomplete(autocomplete.AutocompleteModelBase):
    search_fields = ['^Placa',]
autocomplete.register(Vehiculo, VehiculoAutocomplete)