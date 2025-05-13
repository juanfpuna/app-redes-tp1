from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class ClienteManager(BaseUserManager):
    def create_user(self, documento, password=None, **extra_fields):
        if not documento:
            raise ValueError('El documento debe ser proporcionado.')
        user = self.model(documento=documento, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, documento, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(documento, password, **extra_fields)

class Cliente(AbstractBaseUser, PermissionsMixin):
    TIPO_DOCUMENTO_CHOICES = [
        ('ruc', 'RUC'),
        ('ci', 'Cédula'),
    ]
    id = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    # apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES, default='ci')
    estado = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'documento'
    REQUIRED_FIELDS = ['nombre']  # Campos requeridos al crear un superusuario

    objects = ClienteManager()

    def __str__(self):
        return f'{self.nombre} ({self.documento})'

    def get_full_name(self):
        return f'{self.nombre}'

    def get_short_name(self):
        return self.nombre