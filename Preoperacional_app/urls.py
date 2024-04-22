from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('GeneralForm/', views.FormG, name='FormG'),
    path('InspectionForm/', views.FormI, name='FormI'),
    path('FrontForm/', views.FormFP, name='FormFP'),
    path('SideForm/', views.FormS, name='FormS'),   
    path('BackForm/', views.FormBP, name='FormBP'),
]

