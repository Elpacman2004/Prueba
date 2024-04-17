from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('GeneralForm/', views.FormG, name='FormG'),
    path('InspectionForm/', views.FormI, name='FormI'),
]

