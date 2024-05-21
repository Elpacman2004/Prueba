from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexSPV, name='IndexSPV'),
    path ('GeneralForm_SPV/', views.GeneralForm_SPV, name='General SPV'),
    path ('Staff_requisition/', views.Staff_requisition, name='Staff requisition'),
    path ('Data_of_selected_personnel/', views.Data_of_selected_personnel, name='Data personnel'),
    path ('Conditions_of_employment/', views.Conditions_of_employment, name='Conditions of employment'),
    path ('Salary_assignment/', views.Salary_assignment, name='Salary assignment'),
    path ('Signatures/', views.Signatures, name='Signatures'),    
]