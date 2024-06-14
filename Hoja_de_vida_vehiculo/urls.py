from django.urls import path
from. import views

urlpatterns = [
    path('', views.IndexHVV, name='InexHVV'),
    path('General_data_vehicle', views.General_Data, name='Generalvehicle'),
    path('Docments', views.Docments, name='Docments'),
    path('Tecnical_specifications', views.Tecnical_specifications, name='Tecnical'),
]

