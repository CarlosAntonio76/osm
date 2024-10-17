from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views as v


urlpatterns = [
    path('', v.index, name='index'),
    path('index/', v.index, name='index'),
    path('produtos/', v.index, name='produtos'), 

    path('busca/', v.busca, name='busca'),
    path('<int:produto_id>', v.ver_produtos, name='ver_produtos'),
    path('mensagem/', v.mensagem, name='mensagem'),
]
# Opcao para mostrar imagens
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
