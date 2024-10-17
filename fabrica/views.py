from django.shortcuts import render
from fabrica.models import Fabrica


def fabrica(request):
    fabricas = Fabrica.objects.all()

    return render(request, 'fabrica.html', {'fabricas': fabricas})

