from django.contrib import admin
from .models import Orden, ItemOrden


class ItemsEnOrden(admin.TabularInline):
    model = ItemOrden
    raw_id_fields = ['producto']


@admin.register(Orden)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombres', 'apellidos', 'email',
                    'direccion', 'ciudad', 'pagado',
                    'creado', 'actualizado']
    list_filter = ['pagado', 'creado', 'actualizado']
    inlines = [ItemsEnOrden]
