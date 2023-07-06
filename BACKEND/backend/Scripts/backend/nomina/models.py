from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=255)
    id_empleado = models.IntegerField(unique=True)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    horas_trabajadas = models.IntegerField()
    puesto = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre