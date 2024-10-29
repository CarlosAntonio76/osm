from django.shortcuts import render
from django.http import HttpResponse
from . utils import password_is_valid, email_html
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth
import os
from django.conf import settings
from .models import Ativacao
from hashlib import sha256
from datetime import date, datetime
from datetime import time
from pacotesutil import mostrar_nome_semana as mns  




def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')

        if User.objects.filter(username=username):
            messages.add_message(request, constants.WARNING, f"Usuário {username}, já existe!")
            return redirect('/auth/cadastro')

        existeemail = User.objects.filter(email=email)
        if existeemail:
            messages.add_message(request, constants.WARNING, f"Este email {email}, já existe!")
            return redirect('/auth/cadastro')

        if not password_is_valid(request, senha, confirmar_senha):
            print('Conferindo as senhas: ' ,senha, confirmar_senha)
            return redirect('/auth/cadastro')
   
        try:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=senha,
                                            is_active=False)
            user.save()

            token = sha256(f"{username}{email}".encode()).hexdigest()
            ativacao = Ativacao(token=token, user=user)
            ativacao.save()

            path_template = os.path.join(settings.BASE_DIR, 'autenticacao/templates/emails/cadastro_confirmado.html')
            email_html(path_template, 'Cadastro confirmado', [email,], username=username, link_ativacao=f"http://127.0.0.1:8000/auth/ativar_conta/{token}")

            messages.add_message(request, constants.SUCCESS, "Usuário salvo com sucesso!")
            messages.add_message(request, constants.SUCCESS, "Link enviando para o e-mail cadastrado")

            return redirect('/auth/login')
            
        except Exception as e:
            messages.add_message(request, constants.ERROR, "Erro interno do sistema")
            print('Este é o erro: ', e)
            return redirect('/auth/cadastro')


def login(request):
    if request.method == "GET":
        import locale
        import datetime
        import time
        locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

        nsn = mns.MostrarNomeSemana()
        exibir_semana = mns.MostrarNomeSemana()
        
        print(exibir_semana.nome_semana[nsn.numero_semana])

        exibir_nome_semana = nsn.nome_semana[nsn.numero_semana]


        hora = time.strftime("%H:%M")
        msg = ""

        if hora >= "1" and hora < "12":
            msg = 'Bom dia!'
        elif hora>= "12" and hora < "18":
            msg = 'Boa tarde!'
        elif (hora>"18" and hora<="24") or hora=="0":
            msg = 'Boa noite!'


        if request.user.is_authenticated:
            return redirect('/') # era index
        return render(request, 'login.html', {'msg': msg, 'nome_semana': exibir_nome_semana,
                                              'nsemana': exibir_semana})

    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            print('Teste senhas: ', senha)
            return redirect('/auth/login')
        else:
            auth.login(request, usuario)
            print('deucerto')
            return redirect('/')
        

def ativar_conta(request, token):
    token = get_object_or_404(Ativacao, token=token)
    if token.ativo:
        messages.add_message(request, constants.WARNING, 'Este token já foi usado')
        return redirect('/auth/login')
    user = User.objects.get(username=token.user.username)
    user.is_active = True
    user.save()
    token.ativo = True
    token.save()
    messages.add_message(request, constants.SUCCESS, 'Conta ativa com sucesso')
    return redirect('/auth/login')


    
def sair(request):
    auth.logout(request)
    return redirect('/auth/login')

