from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="facturas.index"), # implementa los metodos GET y POST
    path("<int:pk>", views.show, name="facturas.show"), #Implementa el metodo GET
    path("<int:pk>/update", views.update, name="facturas.update"), #Implementa los metodos PUT y PATCH
    path("<int:pk>/destroy", views.delete, name="facturas.delete"),
    path("<int:pk>/finalizado", views.factura_cerrada, name="compra_finalizada"),
    
    
    #implementar recursos agregar productos - eliminar productos - cerrar compra - anular compra
    path("ventas", views.iniciar_venta, name="iniciar_venta"),
    path("ventas/<int:pk>/pagar", views.cerrar_venta, name="cerrar_venta"),
    path("ventas/productos", views.agregar_producto, name="agregar_producto"),
    path("ventas/<int:pk_factura>/productos", views.quitar_producto, name="quitar_producto"),
    path("ventas/<int:pk_factura>/productos/<int:pk_detalle>", views.actualizar_detalles, name="actualizar_detalles"),
    path("ventas/<int:pk>/anular", views.anular_venta, name="anular_venta"),
    

]