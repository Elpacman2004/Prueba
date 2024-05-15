from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.IndexSPV, name='IndexSPV'),
    path ('GeneralForm_SPV/', views.GeneralForm_SPV, name='General SPV'),
    path ('Staff_requisition/', views.Staff_requisition, name='Staff requisition'),
    path ('Human_Resources/', views.Human_Resources, name='Human Resources'),
    path ('Conditions_of_employment/', views.Conditions_of_employment, name='Conditions of employment'),
]