from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Receita


def index(request):
    tempalte_name = 'index.html'
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    context = {
        'receitas': receitas
    }
    return render(request, tempalte_name, context)


def receita(request, receita_id):
    tempalte_name = 'receita.html'
    receita = get_object_or_404(Receita, pk=receita_id)
    context = {
     'receita': receita
    }
    return render(request, tempalte_name, context)


def buscar(request):
    tempalte_name = 'buscar.html'
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)
    context = {
        'receitas': lista_receitas
        }
    return render(request, tempalte_name, context)
