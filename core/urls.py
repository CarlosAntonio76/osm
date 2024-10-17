from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('autenticacao.urls')),
    path('index/', include('produto.urls')),
    path('cat/', include('categoria.urls')),
    path('fab/', include('fabrica.urls')),
    path('prod/', include('produto.urls')),
    path('', include('osm.urls')),
]

# Opcao para mostrar imagens
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)