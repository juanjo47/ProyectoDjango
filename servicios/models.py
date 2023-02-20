from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length = 100, unique=True)
    def __str__(self):
        return self.nombre

class Tutoriales(models.Model):
    nombre = models.CharField(max_length= 50, unique=True)
    link = models.CharField(max_length=150, unique=True)

class TipoPago(models.TextChoices):
    Efectivo = 'Ef', 'bolivianos',
    Web = 'Ol', 'Dolares',

class DispElec(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    unidades = models.CharField(
        max_length = 2,
        choices= TipoPago.choices, 
        default= TipoPago.Efectivo,
        )
    disponible = models.BooleanField(blank=True, default=True)

class Servicio(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    unidades = models.CharField(
        max_length = 2,
        choices= TipoPago.choices, 
        default= TipoPago.Efectivo,
        )
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)