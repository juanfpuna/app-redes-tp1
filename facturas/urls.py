from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"), # implementa los metodos GET y POST
    path("<int:pk>/update", views.update, name="update"), #Implementa los metodos PUT y PATCH
    path("<int:pk>/destroy", views.delete, name="delete"),

]