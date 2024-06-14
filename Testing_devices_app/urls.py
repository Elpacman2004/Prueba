from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index TD'),
    path('search/', views.Search, name='search'),
    path('IMC/', views.Inspection_Maintenance_Calibration, name='IMC'),   
    path('Add_devices/', views.General_data_device, name='Add_devices'),
    path('DFAD/', views.DFAD, name='DFAD'),
]