from django.shortcuts import render, redirect
from django.contrib.auth.models import User


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
            print("As senha diferem uma da outra")
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuario já cadatsratrado')
            return redirect('cadastro')

        user = User.objects.create_user(
            username=nome,
            email=email,
            password=senha
            )
        user.save()
        print('Ususario cadastrado com sucesso')
        return redirect('cadastro')
    else:
        return render(request, template_name)


def login(request):
    template_name = 'usuarios/login.html'
    return render(request, template_name)


def logout(request):
    pass


def dashboard(request):
    pass
