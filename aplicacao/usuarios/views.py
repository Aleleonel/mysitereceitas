from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from receitas.models import Receita


def cadastro(request):
    template_name = 'usuarios/cadastro.html'
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('O Campo nome não pode ser Nulo!')
            return redirect('cadastro')
        if not email.strip():
            print('O Campo email não pode ser Nulo!')
            return redirect('cadastro')
        if senha != senha2:
            messages.error(request, 'As senha não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(
            username=nome,
            email=email,
            password=senha
            )
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('cadastro')
    else:
        return render(request, template_name)


def login(request):
    template_name = 'usuarios/login.html'
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print("campos senha e email estão vazios")
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list(
                'username', flat=True).get()
            user = authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print("Login realizado com sucesso")
                return redirect('dashboard')
            else:
                return redirect('login')
        else:
            print(email, senha)
            print("email e senha inválidos")
            return redirect('login')
    return render(request, template_name)


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    template_name = 'usuarios/dashboard.html'
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)
        context = {
            'receitas': receitas
        }
        return render(request, template_name, context)
    else:
        return redirect('index')


def cria_receita(request):
    template_name = 'usuarios/cria_receita.html'
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
