from django.db import models

class PaymentInfo(models.Model):
    nombre_titular = models.CharField(max_length=100)
    numero_tarjeta = models.CharField(max_length=19)
    fecha_vencimiento = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre_titular

#registro

class Users(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
