from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=250)
    telefono = models.CharField(max_length=250)

class Encargo(models.Model):
    vehiculo_lista = (
        ("1","AUTO"),
        ("2","MOTO"),
        ("3","CAMIONETA")
    )
    personal_lista = (
        ("1","NAHUEL"),
        ("2","MAXI")

    )
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    vehiculo = models.CharField(max_length=1,choices=vehiculo_lista)
    presupuesto = models.CharField(max_length=50)
    personal =  models.CharField(max_length=1,choices=personal_lista)


    def __str__(self):
        return self.cliente