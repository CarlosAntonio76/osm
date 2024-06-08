from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import views as v


@login_required(login_url='/auth/login')
def teste(request):
    return HttpResponse('Logando com sucesso!')

  