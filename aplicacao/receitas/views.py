from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Receita


def index(request):
    tempalte_name = 'index.html'
    receitas = Receita.objects.all()

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
