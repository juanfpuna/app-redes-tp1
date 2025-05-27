from django.db import models

from clientes.models import Cliente
from productos.models import Producto

# Create your models here.

class Factura(models.Model):
    ESTADO_FACTURA_CHOICES = [
        ('abierta', 'Abierta'),
        ('cerrada', 'Cerrada'),
        ( 'anulada', 'Anulada')
    ]
    
    id = models.AutoField(primary_key=True)
    cod_factura = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, to_field='id', related_name='facturas')
    nombre_empleado = models.CharField(max_length=100, blank=True, null=True)
    total_factura = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    estado = models.CharField(max_length=10, choices=ESTADO_FACTURA_CHOICES, default= 'abierta')
    fecha_emision = models.DateField()

    

    def __str__(self):
        return self.cod_factura
    
class DetalleFactura(models.Model):
    id = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, to_field='id', related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, to_field='id')
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Detalle de {self.factura} - {self.producto.nombre}'
