from decimal import Decimal
from django.conf import settings
from shop.models import Producto


class Carro:
    def __init__(self, request):
        """
        Inicializar carro.
        """
        self.session = request.session
        carro = self.session.get(settings.CART_SESSION_ID)
        if not carro:
            # Inicializar carro vacio
            carro = self.session[settings.CART_SESSION_ID] = {}
        self.carro = carro

    def __iter__(self):
        """
        Iterar sobre los productos del carro y obtener precios 
        desde BD
        """
        productos_ids = self.carro.keys()
        # obtener productos y agregarlos al carro
        productos = Producto.objects.filter(id__in=productos_ids)
        carro = self.carro.copy()
        for producto in productos:
            carro[str(producto.id)]['producto'] = producto
        for item in carro.values():
            item['precio'] = Decimal(item['precio'])
            item['precio_total'] = item['precio'] * item['cantidad']
            yield item

    def __len__(self):
        """
        Cuenta todos los productos (items) del carro
        """
        return sum(item['cantidad'] for item in self.carro.values())

    def agregar(self, producto, cantidad=1, override_quantity=False):
        """
        Agrega un producto al carro o actualiza su cantidad
        """
        producto_id = str(producto.id)
        if producto_id not in self.carro:
            self.carro[producto_id] = {'cantidad': 0,
                                       'precio': str(producto.precio)}
        if override_quantity:
            self.carro[producto_id]['cantidad'] = cantidad
        else:
            self.carro[producto_id]['cantidad'] += cantidad
        self.save()

    def save(self):
        # Marca la sesion como modificada para asegurarse que guarde
        self.session.modified = True

    def quitar(self, producto):
        """
        Quita un producto del carro.
        """
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.save()

    def limpiar(self):
        # Elimina el carro de la sesion
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def obtiene_precio_total(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.carro.values())
