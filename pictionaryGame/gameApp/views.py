from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from django.core import serializers
from gameApp import models
from gameApp.models import Categoria

import random



# Create your views here.
def homePage (request):
    return render(request,'home.html')

def game(request):
    categorias= Categoria.objects.all()
    # categoria = models.get_object_or_404(Categoria,pk=id)
    return render (request,'juego.html',{'categorias':categorias})


def gaming(request, id):
    categoria = get_object_or_404(Categoria,pk=id)
    listado = categoria.listaPalabras.split()
    palabraRandom = random.choice(listado)
    return render (request,'jugando.html', {'categoria':categoria,'listado':listado,'palabraRandom':palabraRandom})

def changeWord(request):
    return render (request,'juego.html')
    


def settings(request):
    return render(request,'config.html')

def do_something():
	print('-------test--------')
 
 