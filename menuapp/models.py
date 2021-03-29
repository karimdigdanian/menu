from django.db import models

class TipoDePlato(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    publicacion = models.DateTimeField('Dia publicado')
    tipo = models.ForeignKey(TipoDePlato, on_delete=models.DO_NOTHING)
    precio = models.IntegerField(default=0)
    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.nombre


    




