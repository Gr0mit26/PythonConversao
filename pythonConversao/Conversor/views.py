from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Moeda
from django.http import HttpResponse
import requests

def Conversor_Moeda(request):
    if request.method == 'POST':
        moedas = Moeda.objects.all()
        quantidade = float(request.POST.get('quantidade'))
        moeda_base = request.POST.get('moeda_base')
        moeda_objetivo = request.POST.get('moeda_objetivo')

        # solicitação api

        api_url = f'https://freecurrencyapi.net/api/v2/convert?apikey=fca_live_JiBxNdOxIDyuSC6vIhjxukELCGzh1oGJjqg1xVxV&q={moeda_base}_{moeda_objetivo}&compact=y'
        response = request.get(api_url)

        if response.status_code == 200:
            data = response.json()
            if f'{moeda_base}_{moeda_objetivo}' in data:
                taxa = data[f'{moeda_base}_{moeda_objetivo}']['val']
                valor_convertido = float(quantidade) * float(taxa)
                context = {
                    'quantidade': quantidade,
                    'moeda_base': moeda_base,
                    'moeda_objetivo': moeda_objetivo,
                    'valor_convertido': valor_convertido,
                }
                return render(request, 'Conversor/Resultado.html', context)
                #return render(request, 'Conversor/Conversor.html', {'moedas': moedas})
            else:
                return HttpResponse("Error: Couldn't find exchange rate.")
        else:
            return HttpResponse("Error: Failed to fetch data from the API.")

    moedas = Moeda.objects.all()  # Obtendo todas as moedas para renderizar o formulário inicial
    return render(request, 'Conversor.html', {'moedas': moedas})
  
   