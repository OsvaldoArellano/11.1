from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'detalle_cliente.html', {'cliente': cliente})

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