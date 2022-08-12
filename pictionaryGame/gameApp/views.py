from django.shortcuts import get_object_or_404, render

from gameApp.models import Categoria

import random


# Create your views here.
def homePage(request):
    return render(request, 'home.html')


def game(request):
    categorias = Categoria.objects.all()
    return render(request, 'juego.html', {'categorias': categorias})


def gaming(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    listado = categoria.listaPalabras.split()
    palabraRandom = random.choice(listado)
    segundos = 0
    if request.GET.get('botonOk'):
        segundos = int(request.GET.get('seconds-timer'))
    else:
        print('not')
    return render(request, 'jugando.html',
                  {'categoria': categoria, 'listado': listado, 'palabraRandom': palabraRandom, 'segundos': segundos})
