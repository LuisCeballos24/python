from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)

class Auto(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    placa = models.CharField(max_length=255)
    vencimiento_placa = models.DateField()
    año_carro = models.IntegerField()