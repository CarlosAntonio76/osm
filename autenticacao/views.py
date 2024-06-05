from django.shortcuts import render
from django.http import HttpResponse
#from . utils import password_is_valid, email_html
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth
import os
from django.conf import settings
#from .models import Ativacao
from hashlib import sha256



def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if User.objects.filter(username=username):
            messages.add_message(request, constants.WARNING, f"Usuário {username}, já existe!")
            return redirect('/auth/cadastro')


def login(request):
    ...

def ativacao(request):
    ...

def ativar_conta(request):
    ...

def sair(request):
    ...