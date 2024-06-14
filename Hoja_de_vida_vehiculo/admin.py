from django.contrib import admin
from .models import General_data, Docments, Tecnical_specifications

# Register your models here.
admin.site.register(General_data)
admin.site.register(Docments)
admin.site.register(Tecnical_specifications)