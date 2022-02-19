
from django.urls import path
from InventarioModel import views
from InventarioModel.views import crear_producto, Venta,borrar_producto,Create_Ventas,Eliminar_Ventas,Update_Ventas

urlpatterns = [
    
    path('', views.vista_inicio, name='inicio'),
    path('inventario', views.vista_inventario, name='inventario'),
    path('crearProducto', views.crear_producto, name='crear_producto'),
    path ('borrarProducto/<id_producto>', views.borrar_producto, name='borrar_producto' ),
    #path('ventas', views.vista_ventas, name='ventas'),
    path('crearVentas', Create_Ventas.as_view(), name='crear_ventas'),
    path('ventas', Venta.as_view(), name='ventas'),
    path('eliminarVentas/<pk>', Eliminar_Ventas.as_view(), name='eliminar_ventas'),
    path('updateVentas/<pk>', Update_Ventas.as_view(), name='update_ventas'),
    
    #path('verVentas',VentasDetailView.as_view(), name='ver_ventas' ) 
    # path('ventas', views.vista_ventas, name='ventas'),
    # path('', views.vista_inicio, name='inicio'),
]