from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views as v


urlpatterns = [
    path('categorias/', v.categoria, name='categoria'),
    path('excluicategoria/<int:id>/', v.excluicategoria, name='excluicategoria'),
    #path('excluircategoria/<int:id>/', v.excluircategoria, name='excluircategoria'),
]


