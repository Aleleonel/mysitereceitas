from django.shortcuts import render


def cadastro(request):
    template_name = 'usuarios/cadastro.html'
    return render(request, template_name)


def login(request):
    template_name = 'usuarios/login.html'
    return render(request, template_name)


def logout(request):
    pass


def dashboard(request):
    pass
