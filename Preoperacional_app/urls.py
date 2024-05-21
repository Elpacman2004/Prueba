from django.urls import path
from. import views

urlpatterns = [
    path('', views.Index_preoperational, name='Index preoperational'),
    path('Search/', views.Search, name='Search'),
    path('GeneralForm/', views.FormG, name='FormG'),
    path('InspectionForm/', views.FormI, name='FormI'),
    path('FrontForm/', views.FormFP, name='FormFP'),
    path('SideForm/', views.FormS, name='FormS'),   
    path('BackForm/', views.FormBP, name='FormBP'),
]

