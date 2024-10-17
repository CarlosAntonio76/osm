#encoding: utf-8
# -*- coding: utf-8 -*- 
from django.shortcuts import render, HttpResponse, redirect
from categoria.models import Categoria
from django.contrib import messages
from django.contrib.messages import constants
from datetime import date, datetime
from datetime import time
    

def categoria(request):
    template_name = 'categorias.html'
    import locale
    import datetime
    import time
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
     
    datas = time.strftime("%A, %d %B %Y %H:%M:%S")
   
    dia_semana = datetime.datetime.today().weekday()

    if dia_semana == 0:
        print("Segunda-Feira")
    elif dia_semana == 1:
        print("Terça-Feira")
    elif dia_semana == 2:
        print("Quarta-Feira")
    elif dia_semana == 3:
        print("Quinta-Feira")
    elif dia_semana == 4:
        print("Sexta-Feira")
    elif dia_semana == 5:
        print("Sábado")
    elif dia_semana == 6:
        print("Domingo")

    dt = datetime.datetime.now()

    weekday_name = ["Domingo", "Segunda-Feira",
                    "Terça-Feira","Quarta-Feira",
                    "Quinta-Feira","Sexta-Feira",
                    "Sábado"]
    
    wk_num = int(dt.strftime("%w"))
    print('Hoje é.:', weekday_name[wk_num])

                     
    object_list = Categoria.objects.all()
    status = request.POST.getlist('status')

    
    if request.method=='POST':
         status = request.POST.getlist('status')
         object_list = object_list.all()
    
    if status ==['T', 'A', 'I']:
         object_list = object_list.all()
    
    if status ==[]:
         messages.add_message(request, constants.ERROR, 'Sem dados para serem exibidos! - Selecione um Filtro')
         object_list = object_list.none()


    if status == ['T']:
        object_list = object_list.all()

    if status == ['A']:
        object_list = object_list.filter(ativo=True)

    if status == ['I']:
        object_list = object_list.filter(ativo=False)
    
    object_list = {'object_list': object_list, 'selected_status': status, 'datas': datas}
    print(status)

    return render(request, template_name, object_list)
