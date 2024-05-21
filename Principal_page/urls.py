from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
]
handler404 = 'Principal_page.views.handler404'