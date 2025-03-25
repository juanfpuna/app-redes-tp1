from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=80)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre