from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['nombre']
        indexes = [
            models.Index(fields=['nombre']),
        ]
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse(
            'shop:lista_producto_por_categoria', args=[self.slug]
            #'shop:product_list_by_category', args=[self.slug]
        )


class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        related_name='productos',
        on_delete=models.CASCADE
    )
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    imagen = models.ImageField(
        upload_to='productos/%Y/%m/%d',
        blank=True
    )
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['nombre']),
            models.Index(fields=['-creado']),
        ]

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('shop:detalle_producto', args=[self.id, self.slug])
        #return reverse('shop:product_detail', args=[self.id, self.slug])