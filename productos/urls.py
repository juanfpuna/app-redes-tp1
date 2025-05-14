from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>", views.show, name="show"),
    path("<int:pk>/update", views.update, name="update"),
    path("<int:pk>/destroy", views.delete, name="delete"),
    
]
