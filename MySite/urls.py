from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('admin/', admin.site.urls),
        path('', include('Principal_page.urls')),
        path('Preoperational/', include('Preoperacional_app.urls')),
        path('SPV/', include('SPV_app.urls')),
        path('Testing devices/', include('Testing_devices_app.urls')),
        path('Vehicle_service_history/', include('Hoja_de_vida_vehiculo.urls')),
        path('Computer_equipment_maintenance/', include('Mtto_equipos_de_computo.urls')),
        path('Pre_operational_inspection_measurement_equipment/', include('Pre_Op_equipos_medicion_app.urls')),
        path('\nRequest_for_HTA_Equipment_and_Others/', include('Solicitud_de_equipos_app.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
else:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('Preoperacional_app.urls')),
        path('SPV/', include('SPV_app.urls')),
        path('Testing devices/', include('Testing_devices_app.urls')),
        path('Vehicle_service_history/', include('Hoja_de_vida_vehiculo.urls')),
        path('\nRequest_for_HTA_Equipment_and_Others/', include('Solicitud_de_equipos_app.urls')),
    ]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_url=settings.MEDIA_ROOT)