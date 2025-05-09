from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"), # implementa los metodos GET y POST
    path("<int:pk>/show", views.show, name="show"), #Implementa el metodo GET
    path("<int:pk>/update", views.update, name="update"), #Implementa los metodos PUT y PATCH
    path("<int:pk>/destroy", views.delete, name="delete"),
    
    #implementar recursos agregar productos - eliminar productos - cerrar compra - anular compra
    path("ventas", views.iniciar_venta, name="iniciar_venta"),
    path("ventas/<int:pk>", views.cerrar_venta, name="cerrar_venta"),
    path("ventas/<int:pk>/productos", views.agregar_producto, name="agregar_producto"),
    path("ventas/<int:pk_factura>/productos/<int:pk_detalle>", views.actualizar_detalles, name="actualizar_detalles"),
    path("ventas/<int:pk>/anular", views.anular_venta, name="anular_venta"),
    

]