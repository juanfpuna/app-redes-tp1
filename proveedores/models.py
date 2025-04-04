from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre