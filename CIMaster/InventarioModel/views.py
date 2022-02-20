from time import sleep
#from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.views import LogoutView
from .forms import ProductoForm, UserRegistrationForm
from .models import Producto,Ventas
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView

#Vistas basadas en funciones. se dejo una a modo de demostracion de uso.

def vista_inicio (request ):
    return render (request, 'inicio.html')

def vista_inventario (request ):
    return render (request, 'inventario.html', {'Producto': Producto.objects.all()})
@login_required
def vista_ventas (request ):
    return render (request, 'ventas.html', {'Ventas': Ventas.objects.all()})
@login_required
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
@login_required
def borrar_producto (request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    producto.delete()
    return redirect('inventario')

# PEDASO DE CODIGO COMENTADO SIN FUNCIONAR
# def actualizar_producto (request, id_producto):
#     producto = Producto.objects.get(id=id_producto)
#     if request.method == 'POST':
            
#         formulario_producto = ProductoForm(request.POST)
        
#         if formulario_producto.is_valid():
            
#             data = formulario_producto.cleaned_data
#             producto.objects.update(nombre = data['nombre'], descripcion = data['descripcion'], tipo=data['tipo'], cantidad=data['cantidad'] )
#             return redirect ('inventario')                 
#     else: 
#         formulario_producto = ProductoForm()
    
#     return render(request, 'crear_producto.html',{'formulario':formulario_producto})


# MBV  Ventas Inicio
class Venta(ListView ):
    model = Ventas
    template_name = "ventas.html"
    context_object_name = 'ventas'
    
class VentasDetailView (LoginRequiredMixin,DetailView):
    
    model = Ventas
    template_name = "ver_ventas.html"
    
    
class Create_Ventas(LoginRequiredMixin,CreateView):
       
    model = Ventas
    fields = ['nombre_producto','precio_producto','cantidades','vendedor_id']
    success_url = reverse_lazy("ventas")
    template_name = "crear_venta.html" 
    
class Update_Ventas(LoginRequiredMixin,UpdateView):
           
    model = Ventas
    fields = ['nombre_producto','cantidades']
    success_url = reverse_lazy("ventas")
    template_name = "crear_venta.html" 
    
class Eliminar_Ventas(LoginRequiredMixin,DeleteView):
           
    model = Ventas
    success_url = reverse_lazy("ventas")
    template_name = "eliminar_venta.html" 

#LOGIN INICIO
 
def login_request (request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
         
        if form.is_valid():
            
            usuario = form.cleaned_data['username']
            contrasena = form.cleaned_data['password']
             
            user = authenticate(username = usuario, password = contrasena)
            
            if user is not None:
            
                login(request, user)
                return redirect('inicio')
                
            else:
                return render(request, 'login.html',{'form':form,'Error':'Usuario y Contraseña invalido'})   
            
        else:
            return render(request, 'login.html',{'form':form})   
                          
    else:
        form = AuthenticationForm()
        return render(request, 'login.html',{'form':form})             
    
    
# REGISTRO

def register(request):
    # print('antes de if1')
    if request.method == 'POST':
        
        form = UserRegistrationForm(request.POST)
        # print('antes de if2')
        if form.is_valid():
            usuario: form.cleaned_data['username']
            # print('antes de save')
            form.save()
            # print('antes de redirect')
            return redirect('login')
        else:
            # print('formulario no valido')
            return  render(request, 'registro.html', {'form':form})
    else:   
        # print('despues de else')
        form = UserRegistrationForm()

    
        return render(request, 'registro.html', {'form':form})
    
#LOGOUT

# class LogOut (LogoutView):
    
#     print('')