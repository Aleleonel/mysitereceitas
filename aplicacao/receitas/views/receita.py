from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from receitas.models import Receita
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    tempalte_name = 'receitas/index.html'
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    paginator = Paginator(receitas, 3)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    context = {
        'receitas': receitas_por_pagina
    }
    return render(request, tempalte_name, context)


def receita(request, receita_id):
    tempalte_name = 'receitas/receita.html'
    receita = get_object_or_404(Receita, pk=receita_id)
    context = {
     'receita': receita
    }
    return render(request, tempalte_name, context)


def cria_receita(request):
    template_name = 'receitas/cria_receita.html'
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(
            pessoa=user,
            nome_receita=nome_receita,
            ingredientes=ingredientes,
            modo_preparo=modo_preparo,
            tempo_preparo=tempo_preparo,
            rendimento=rendimento,
            categoria=categoria,
            foto_receita=foto_receita)
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, template_name)

    return render(request, template_name)


def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')


def edita_receita(request, receita_id):
    template_name = "receitas/edita_receita.html"
    receita = get_object_or_404(Receita, pk=receita_id)
    context = {
        'receita': receita
    }

    return render(request, template_name, context)


def atualiza_receita(request):
    if request.method == "POST":
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        r.save()
        return redirect('dashboard')
