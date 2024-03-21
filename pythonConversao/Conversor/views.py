from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Moeda

def Conversor_Moeda(request):
    moedas = Moeda.objetcts.all()
    return render(request, 'Conversor/Conversor.html', {'moedas': moedas})