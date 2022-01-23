from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

# Create your views here.

def vista_inicio (request ):
    return render (request, 'inicio.html')

def vista_inventario (request ):
    return render (request, 'inventario.html')