from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.lista_producto, name='lista_producto'),
    path('<slug:category_slug>/', views.lista_producto,
         name='lista_producto_por_categoria'),
    path('<int:id>/<slug:slug>/', views.detalle_producto,
         name='detalle_producto'),
]