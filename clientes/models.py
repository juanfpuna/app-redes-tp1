from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'