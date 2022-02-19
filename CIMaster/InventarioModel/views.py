from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import ProductoForm
from .models import Producto,Ventas
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView

# Create your views here.

def vista_inicio (request ):
    return render (request, 'inicio.html')

def vista_inventario (request ):
    return render (request, 'inventario.html', {'Producto': Producto.objects.all()})

def vista_ventas (request ):
    return render (request, 'ventas.html', {'Ventas': Ventas.objects.all()})

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

def borrar_producto (request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    producto.delete()
    return redirect('inventario')



class Venta(ListView):
    model = Ventas
    template_name = "ventas.html"
    context_object_name = 'ventas'
    
class VentasDetailView (DetailView):
    
    model = Ventas
    template_name = "ver_ventas.html"
    
    
class Create_Ventas(CreateView):
       
    model = Ventas
    fields = ['nombre_producto','precio_producto','cantidades','vendedor_id']
    success_url = reverse_lazy("ventas")
    template_name = "crear_venta.html" 
    
class Update_Ventas(UpdateView):
           
    model = Ventas
    fields = ['nombre_producto','cantidades']
    success_url = reverse_lazy("ventas")
    template_name = "crear_venta.html" 
    
class Eliminar_Ventas(DeleteView):
           
    model = Ventas
    success_url = reverse_lazy("ventas")
    template_name = "ver_ventas.html" 
    
    
