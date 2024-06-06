from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('osm.urls')),
    path('autenticacao/', include('autenticacao.urls')),
    path('admin/', admin.site.urls),
]
