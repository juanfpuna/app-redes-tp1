from django.contrib import admin
# include necessary libraries
from django.urls import path, include

from rest_framework import routers
 
# import everything from views
from .views import *
 
# define the router
router = routers.DefaultRouter()
 
urlpatterns = [
    path('admin/', admin.site.urls),
    # add apis urls
    path('', include("apis.urls"))
]