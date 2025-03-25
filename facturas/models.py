from django.db import models

from clientes.models import Cliente

# Create your models here.

class Factura(models.Model):
    numero = models.CharField(max_length=80)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.numero