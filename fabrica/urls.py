from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views as v


urlpatterns = [
    path('fabrica/', v.fabrica, name='fabrica'),
]
