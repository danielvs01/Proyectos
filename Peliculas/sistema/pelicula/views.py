from django.shortcuts import render
from django.http import HttpResponse
from .models import Pelicula
# Create your views here.

def inicio(request):
    return render(request, "paginas/inicio.html")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, "peliculas/index.html", {'peliculas': peliculas})