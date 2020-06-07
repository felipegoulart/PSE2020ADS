from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User, UnicodeUsernameValidator

from django.contrib import messages

from painel import views 


def pag_login(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario').lower()
        senha = request.POST.get('senha')
        user = authenticate(request, username=usuario, password=senha)

        if User.objects.filter(username=usuario).exists():
            if user is not None:
                login(request, user)
                return redirect('painel')
            else:
                messages.add_message(request, messages.ERROR, 'Senha inválida')
                return render(request, 'login.html')
        else:
            messages.add_message(request, messages.ERROR, 'Usuário inválido')
            return render(request, 'login.html')

    return render(request, 'login.html')


def pag_registrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        usuario = request.POST.get('usuario').lower()
        senha = request.POST.get('senha')
        senha_repetida = request.POST.get('senha_repetida')

        if not nome or not sobrenome or not usuario or not senha or not senha_repetida:
            messages.add_message(request, messages.ERROR, 'Preencha todos os CAMPOS')
            return render(request, 'registrar.html')
        
        if len(usuario) < 6:
            messages.add_message(request, messages.ERROR, 'O usuário deve ter mais que 6 dígitos')
            return render(request, 'registrar.html')

        if User.objects.filter(username=usuario).exists():
            messages.add_message(request, messages.ERROR, 'Usuário já existe')
            return render(request, 'registrar.html')

        if len(senha) < 8:
            messages.add_message(request, messages.ERROR, 'A senha deve conter 8 digitos')
            return render(request, 'registrar.html')

        if senha.isalpha():
            messages.add_message(request, messages.ERROR, 'A senha deve conter números')
            return render(request, 'registrar.html')
        
        if senha.isnumeric():
            messages.add_message(request, messages.ERROR, 'A senha deve conter letras')
            return render(request, 'registrar.html')

        if senha != senha_repetida:
            messages.add_message(request, messages.ERROR, 'As senhas devem ser iguais')
            return render(request, 'registrar.html')

        user = User.objects.create_user(username=usuario, email=None, password=senha,
                                        first_name=nome, last_name=sobrenome)
        user.save()

        messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com SUCESSO!')
        return redirect('login')

    return render(request, 'registrar.html')


def pag_recuperar_senha(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario').lower()
        
        if User.objects.filter(username=usuario).exists():
            senha = request.POST.get('senha')
            senha_repetida = request.POST.get('senha_repetida')
            
            if len(senha) < 8:
                messages.add_message(request, messages.ERROR, 'A senha deve ter 8 digitos')
                return render(request, 'recuperacao.html')

            if senha.isalpha():
                messages.add_message(request, messages.ERROR, 'A senha deve ter números')
                return render(request, 'recuperacao.html')
            
            if senha.isnumeric():
                messages.add_message(request, messages.ERROR, 'A senha deve ter letras')
                return render(request, 'recuperacao.html')

            if senha != senha_repetida:
                messages.add_message(request, messages.ERROR, 'As senhas devem ser iguais')
                return render(request, 'recuperacao.html')

            user = User.objects.get(username=usuario)
            user.set_password(senha)
            user.save()

            messages.add_message(request, messages.SUCCESS, 'Senha alterada com SUCESSO!')
            return redirect('login')

        else:
            messages.add_message(request, messages.ERROR, 'Usuário NÃO existe')
            return render(request, 'recuperacao.html')

    return render(request, 'recuperacao.html')
