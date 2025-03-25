from django.db import models

# Create your models here.
class Cliente(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('ruc', 'RUC'),
        ('cedula', 'Cédula'),
    ]
   
    documento = models.CharField(max_length=20, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.documento})'