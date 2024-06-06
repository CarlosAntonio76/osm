from django.urls import path
from . import views as v

urlpatterns = [
    path('cadastro/', v.cadastro, name='cadastro'),
    path('login/', v.login, name='login'),
    path('ativar_conta/<str:token>/', v.ativar_conta, name='ativar_conta'),
    path('sair/', v.sair, name='sair'),
]
