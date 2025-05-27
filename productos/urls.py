from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="productos"),
    path("<int:pk>", views.show, name="producto.ver"),
    path("<int:pk>/update", views.update, name="producto.actualizar"),
    path("<int:pk>/destroy", views.delete, name="producto.eliminar"),
    path("crear", views.create, name="producto.crear"),
    
]
