from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='IndexSE'),
    path('SearchSE/<str:model_name>/', views.searchSE, name='SearchSE'),
    path('General_data', views.GeneralDataSE, name='ChoisesFields'),
    path('Equipment', views.Equipment_view , name='Equipment'),
    path('Tools_and_accessories', views.ToolsAndAccessories, name='ToolsAndAccessories'),
    path('Safety_equipment', views.SafetyEquipment_view, name='SafetyEquipment'),
    path('Vehicle_logistics', views.VehicleLogistics_view   , name='VehicleLogistics'),
    
]