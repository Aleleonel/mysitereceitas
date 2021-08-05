from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    tempalte_name = 'index.html'
    receitas_dinamicas = {
        1: 'Carne de Panel',
        2: 'Lazanha',
        3: 'Costelinha Agre-Doce',
        4: 'Bolo de Chocolate'
    }
    context = {
        'nome_receitas': receitas_dinamicas
    }
    return render(request, tempalte_name, context)


def receita(request):
    return render(request, 'receita.html')
