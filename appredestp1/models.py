from django.db import models
# clientes/admin.py
from django.contrib import admin
from .models import Cliente

admin.site.register(Cliente)

# facturas/admin.py
from django.contrib import admin
from .models import Factura

admin.site.register(Factura)

# productos/admin.py
from django.contrib import admin
from .models import Producto

admin.site.register(Producto)