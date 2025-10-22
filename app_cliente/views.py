from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Vehiculo
from .forms import ClienteForm, VehiculoForm

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    # mostramos el detalle y la lista de vehiculos relacionados
    return render(request, 'detalle_cliente.html', {'cliente': cliente})


def agregar_vehiculo(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            vehiculo.cliente = cliente
            vehiculo.save()
            return redirect('app_cliente:detalle_cliente', cliente_id=cliente.id)
    else:
        form = VehiculoForm()
    return render(request, 'agregar_vehiculo.html', {'form': form, 'cliente': cliente})


def eliminar_vehiculo(request, cliente_id, vehiculo_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id, cliente=cliente)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('app_cliente:detalle_cliente', cliente_id=cliente.id)
    # Podrías añadir una plantilla de confirmación; por ahora redirigimos en GET
    return redirect('app_cliente:detalle_cliente', cliente_id=cliente.id)

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_cliente:listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'formulario_cliente.html', {'form': form, 'titulo': 'Crear cliente'})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('app_cliente:detalle_cliente', cliente_id=cliente.id)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'formulario_cliente.html', {'form': form, 'titulo': 'Editar cliente'})

def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('app_cliente:listar_clientes')
    return render(request, 'confirmar_borrar.html', {'cliente': cliente})