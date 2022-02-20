
from django.urls import path
from InventarioModel import views
from InventarioModel.views import acerca_de,crear_producto, Venta,borrar_producto,Create_Ventas,Eliminar_Ventas,Update_Ventas,VentasDetailView,register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', views.vista_inicio, name='inicio'),
    
    path('login', views.login_request, name='login'),
    path('register',views.register, name='register'),
    path('logout',LogoutView.as_view(), name='logout'),
    
    path('acerca_de', views.acerca_de,name='acerca_de' ),
    
    path('inventario', views.vista_inventario, name='inventario'),
    path('producto/crear', views.crear_producto, name='crear_producto'),
    path ('producto/eliminar/<id_producto>', views.borrar_producto, name='borrar_producto' ),
    # path('producto/actualizar/<id_producto>', views.actualizar_producto, name= 'actualizar_producto'),
    #path('ventas', views.vista_ventas, name='ventas'),
    path('ventas/crear', Create_Ventas.as_view(), name='crear_ventas'),
    path('ventas', Venta.as_view(), name='ventas'),
    path('ventas/eliminar//<pk>', Eliminar_Ventas.as_view(), name='eliminar_ventas'),
    path('ventas/actualizar/<pk>', Update_Ventas.as_view(), name='update_ventas'),
    path('ventas/visualizar/<pk>',VentasDetailView.as_view(), name='ver_ventas' ) ,
    # path('ventas', views.vista_ventas, name='ventas'),
    # path('', views.vista_inicio, name='inicio'),
]
handler404 = "django_404_project.views.page_not_found_view"