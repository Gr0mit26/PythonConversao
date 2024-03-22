from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Moeda
from django.http import HttpResponse
import requests
import freecurrencyapi

def Conversor_Moeda(request):
    if request.method == 'POST':
        moedas = Moeda.objects.all()
        quantidade_str = float(request.POST.get('quantidade_str'))
        moeda_base = request.POST.get('moeda_base')
        moeda_objetivo = request.POST.get('moeda_objetivo')
        
        try:
            quantidade = float(quantidade_str)
        except ValueError:
            return HttpResponse("Error: Quantidade inválida.")

        # solicitação api

        client = freecurrencyapi.Client('fca_live_JiBxNdOxIDyuSC6vIhjxukELCGzh1oGJjqg1xVxV')

        try:
            result = client.latest()
        except freecurrencyapi.exceptions.RequestError as e:
            return HttpResponse(f"Error: Failed to fetch data from the API. Details: {str(e)}")
        
        print(result)
        
        if moeda_objetivo in result['data']:
            taxa_inicial = result['data'][moeda_base]
            taxa = result['data'][moeda_objetivo]
            valor_convertido = (quantidade / taxa_inicial) * taxa
            context = {
                'quantidade': quantidade,
                'moeda_base': moeda_base,
                'moeda_objetivo': moeda_objetivo,
                'valor_convertido': valor_convertido,
            }
            return render(request, 'Resultado.html', context)
        else:
            return HttpResponse("Error: Couldn't find exchange rate.")

    moedas = Moeda.objects.all()  
    return render(request, 'Conversor.html', {'moedas': moedas})
  
   