from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.store, name="store"),
    path("<int:pk>/", views.update, name="update"),
    path("<int:pk>/", views.delete, name="delete"),

]
