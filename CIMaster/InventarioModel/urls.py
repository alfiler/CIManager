

from django.urls import path
from InventarioModel import views

urlpatterns = [
    
    path('', views.vista_inicio, name='inicio'),
    path('inventario', views.vista_inventario, name='inventario'),
    # path('ventas', views.vista_ventas, name='ventas'),
    # path('', views.vista_inicio, name='inicio'),
]