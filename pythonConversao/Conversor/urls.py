from django.urls import path
from . import views

urlpatterns = [
    path('', views.Conversor_Moeda, name='Conversor_Moeda'),
]