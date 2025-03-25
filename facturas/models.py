from django.db import models

from clientes.models import Cliente
from productos.models import Producto

# Create your models here.

class Factura(models.Model):
    cod_factura = models.CharField(max_length=20, unique=True)
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, to_field='documento')
    nombre_empleado = models.CharField(max_length=100)
    total_factura = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.cod_factura
    
class DetalleFactura(models.Model):
    cod_factura = models.ForeignKey(Factura, on_delete=models.CASCADE, to_field='cod_factura')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Detalle de {self.cod_factura} - {self.producto.nombre}'
