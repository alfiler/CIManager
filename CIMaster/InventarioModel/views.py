from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import ProductoForm
from .models import Producto

# Create your views here.

def vista_inicio (request ):
    return render (request, 'inicio.html')

def vista_inventario (request ):
    return render (request, 'inventario.html', {'Producto': Producto.objects.all()})

def crear_producto(request):
    
    if request.method == 'POST':
    
        formulario_producto = ProductoForm(request.POST)
        
        if formulario_producto.is_valid():
            
            data = formulario_producto.cleaned_data
            Producto.objects.create(nombre = data['nombre'], descripcion = data['descripcion'], tipo=data['tipo'], cantidad=data['cantidad'] )
            return redirect ('inventario')                 
    else: 
        formulario_producto = ProductoForm()
    
    return render(request, 'crear_producto.html',{'formulario':formulario_producto})