#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime

from django.contrib.auth.models import User
from django.contrib import auth

from django.core.paginator import Paginator
from produto.models import Produtos

from django.db.models import Q, Value
from django.db.models.functions import Concat


@login_required(login_url='/auth/login')
def index(request):
    import sys
    import locale
    import datetime
    import time
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
     
    datas = time.strftime("%A, %d %B %Y %H:%M:%S")

    busca = request.GET.get('busca')
    
    if busca:
        produto_list = Produtos.objects.filter(descricao__icontains=busca)
    else:
        produto_list = Produtos.objects.all()

    paginator = Paginator(produto_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj, 'datas': datas})


def mensagem(request):
    context = 'Pagina em construção, volte depois'
    return render(request, 'mensagem.html', {'context': context})


def ver_produtos(request, produto_id):
    try:
        contatos = Produtos.objects.get(id=produto_id)

        if not contatos.mostrar:
            raise Http404("Provavelmente o código do cliente não existe")

    except Produtos.DoesNotExist:
        raise Http404("Provavelmente o código do cliente não existe")
    return render(request, 'ver_produtos.html', {
                  'contatos': contatos
    })



def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Campo termo não pode ficar vazio.'
        )
        return redirect('index')

    campos = Concat('descricao', Value(' '), 'descricao')

    contatos = Produtos.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(descricao__icontains=termo)
    )

    #contatos = Produtos.objects.order_by('id').filter(
    #    Q(descricao__icontains=termo) | Q(descricao__icontains=termo),
    #    mostrar=True
    #)

    paginator = Paginator(contatos, 8)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'busca.html', {
        'contatos': contatos
    })


