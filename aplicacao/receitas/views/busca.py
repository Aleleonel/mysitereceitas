from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from receitas.models import Receita


def busca(request):
    tempalte_name = 'receitas/buscar.html'
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)
    context = {
        'receitas': lista_receitas
        }
    return render(request, tempalte_name, context)
