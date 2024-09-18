from django.urls import path
from . import views

urlpatterns = [
    path('', views.PreOp_equpment, name='PreOp_equpment'),
]