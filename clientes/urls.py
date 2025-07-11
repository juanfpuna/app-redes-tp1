from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/show", views.show, name="show"),
    path("<int:pk>/update", views.update, name="update"),
    path("<int:pk>/destroy", views.destroy, name="destroy"),
    path("autenticarse/", views.autenticarse, name="autenticarse"),
    path('perfil', views.perfil, name='perfil')
    
]
