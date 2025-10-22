from django.urls import path
from . import views

app_name = 'app_cliente'

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('cliente/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('crear/', views.crear_cliente, name='crear_cliente'),
    path('editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('borrar/<int:cliente_id>/', views.borrar_cliente, name='borrar_cliente'),
]