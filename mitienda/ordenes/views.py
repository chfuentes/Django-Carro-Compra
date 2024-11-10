from django.shortcuts import render
from .models import ItemOrden
from .forms import FormCrearOrden
# from .tasks import order_created
from carro.carro import Carro


def crear_orden(request):
    carro = Carro(request)
    if request.method == 'POST':
        form = FormCrearOrden(request.POST)
        if form.is_valid():
            orden = form.save()
            for item in carro:
                ItemOrden.objects.create(orden=orden,
                                         producto=item['producto'],
                                         precio=item['precio'],
                                         cantidad=item['cantidad'])
            # Limpiar carro
            carro.limpiar()
            # Lanzar tarea asincrona
            # order_created.delay(order.id)
            return render(request,
                          'ordenes/orden/creada.html',
                          {'orden': orden})
    else:
        form = FormCrearOrden()
    return render(request,
                  'ordenes/orden/crear.html',
                  {'carro': carro, 'form': form})
