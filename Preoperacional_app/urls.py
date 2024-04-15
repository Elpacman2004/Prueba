from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('GeneralForm/', views.FormG, name='FormG'),
    path('InspectionForm/', views.FormI, name='FormI'),
    path('FormFrontPart/', views.FormFP, name='FormFP'),
    path('FormSidePart/', views.FormSP, name='FormSP'),
    path('FormBackPart/', views.FormBP, name='FormBP'),
]

