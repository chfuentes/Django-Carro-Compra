from django.urls import path
from . import views

app_name = 'carro'

urlpatterns = [
    path('', views.detalle_carro, name='detalle_carro'),
    path('agregar/<int:producto_id>/',
         views.agregar_a_carro, name='agregar_a_carro'),
    path('quitar/<int:producto_id>/', views.quitar_de_carro,
         name='quitar_de_carro'),
]
