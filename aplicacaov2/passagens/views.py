from django.shortcuts import render
from passagens.forms import PassagemForms


def index(request):
    template_name = 'index.html'
    form = PassagemForms()
    context = {
        'form': form
        }
    return render(request, template_name, context)


def revisao_consulta(request):
    template_name = 'consulta.html'
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        if form.is_valid():
            context = {
                'form': form
                }
            return render(request, template_name, context)
        else:
            print('Form Inválido')
            template_name = 'index.html'
            context = {
                'form': form
                }
            return render(request, template_name, context)
