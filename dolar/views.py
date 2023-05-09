from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import requests

def cotacao_dolar(request):
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisicao = requests.get(link)
    informacoes = requisicao.json()
    cotacao = informacoes['USDBRL']['ask']
    cotacao = float(cotacao)

    context = {'cotacao':cotacao}
    if request.method == 'POST':
        real = float(request.POST['real'])
        dolar = round(real / cotacao, 2)

        context['real'] = real
        context['dolar'] = dolar
        return render(request, 'dolar/dolar.html', context)
    return render(request, 'dolar/dolar.html', context)

def cotacao_real(request):
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisicao = requests.get(link)
    informacoes = requisicao.json()
    cotacao = informacoes['USDBRL']['ask']
    cotacao = float(cotacao)

    context = {'cotacao': cotacao}
    if request.method == 'POST':
        dolar = float(request.POST['dolar'])
        real = round(dolar * cotacao, 2)
        context['real'] = real
        context['dolar'] = dolar

        return render(request, 'dolar/real.html', context)
    return render(request, 'dolar/real.html', context)

    #converte = int(input("Insira > "))
    #convertido = converte / cotacao
    #print(round(convertido, 2))
