from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout

from django.contrib import messages

from login import views
from .models import Arquivos
from .forms import ArquivosForm
from .dash_app.graficos import NomeArquivo


@login_required(login_url='login')
def painel(request):
    arquivos_nomes = Arquivos.objects.all()
    return render(request, 'painel.html', {'arquivos_nomes': arquivos_nomes})


@login_required(login_url='login')
def add_arquivos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        arq = request.FILES.get('arquivo')
        u = request.user

        if not nome:
            messages.add_message(request, messages.ERROR, 'Nome do arquivo OBRIGATÓRIO')
            return render(request, 'add_arquivo.html')

        elif not arq:
            messages.add_message(request, messages.ERROR, 'Insira um ARQUIVO')
            return render(request, 'add_arquivo.html')

        else:

            if arq.name[-3:] == 'csv':
                arq.name = nome + '.csv'
                form = Arquivos(nome= nome, arquivos= arq, user= u)
                form.save()

                return redirect('painel')
            
            else:
                messages.add_message(request, messages.ERROR, 'Tipo de arquivo INVÁLIDO')
                return render(request, 'add_arquivo.html')

    return render(request, 'add_arquivo.html')


@login_required(login_url='login')
def dash(request, id):
    arquivo = Arquivos.objects.get(id= id)
    NomeArquivo(arquivo)
    return render(request, 'dash.html', {'arquivo' : arquivo})



def logout_view(request):
    logout(request)
    return redirect('login')


def deletar(request, id):
    try:
        arq = Arquivos.objects.get(id= id)
        arq.arquivos.delete(save=False)
    except:
        pass

    get_object_or_404(Arquivos, id=id).delete()

    return redirect('painel')
