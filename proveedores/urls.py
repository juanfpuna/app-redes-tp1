from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="proveedores.index"),
    path("<int:pk>/show", views.show, name="show"),
    path("<int:pk>/update", views.update, name="update"),
    path("<int:pk>/destroy", views.delete, name="delete"),
    path("crear", views.create, name="create"),

]
