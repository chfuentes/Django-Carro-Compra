from django.db import models
from shop.models import Producto


class Orden(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    direccion = models.CharField(max_length=250)
    # postal_code = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    pagado = models.BooleanField(default=False)

    class Meta:
        ordering = ['-creado']
        indexes = [
            models.Index(fields=['-creado']),
        ]

    def __str__(self):
        return f'Orden {self.id}'

    def obtiene_costo_total(self):
        return sum(item.obtiene_costo() for item in self.items.all())


class ItemOrden(models.Model):
    orden = models.ForeignKey(Orden,
                              related_name='items',
                              on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,
                                 related_name='items_orden',
                                 on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10,
                                 decimal_places=2)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def obtiene_costo(self):
        return self.precio * self.cantidad
