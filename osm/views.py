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

from django.db.models import Q, Value
from django.db.models.functions import Concat



@login_required(login_url='/auth/login')
def dashboard(request):
    import locale
    import time
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

    hora = time.strftime("%H:%M")

    if hora >= "18":
        print('Boa noite Galera!')
    elif hora >= "24":
        print('Bom dia Galera!')
    elif hora >= "12":
        print('Boa tarde Galera!')
  
     
    datas = time.strftime("%A, %d %B %Y %H:%M:%S")
    context = {'autor': 'carlos'}
    
    return render(request, 'dashboard.html', {'context': context, 'datas': datas})

