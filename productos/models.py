from django.db import models

# Create your models here.
class Producto(models.Model):
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre