from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Producto
from .carro import Carro
from .forms import FormAgregarProductoCarro


@require_POST
def agregar_a_carro(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    form = FormAgregarProductoCarro(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        carro.agregar(producto=producto,
                      cantidad=cd['cantidad'],
                      override_quantity=cd['override'])
    return redirect('carro:detalle_carro')


@require_POST
def quitar_de_carro(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.quitar(producto)
    return redirect('carro:detalle_carro')


def detalle_carro(request):
    carro = Carro(request)
    for item in carro:
        item['actualizar_cantidad_form'] = FormAgregarProductoCarro(initial={
            'cantidad': item['cantidad'],
            'override': True})
    return render(request, 'carro/detalle.html', {'carro': carro})
