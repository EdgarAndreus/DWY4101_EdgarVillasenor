from django.shortcuts import render, redirect
from .models import *
from .forms import ClienteForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


def home(request):
    return render(request, 'tienda/index.html')


def productos(request):
    producto = Producto.objects.all()
    cliente = Cliente.objects.all()
    context = {'producto': producto, 'cliente': cliente}
    return render(request, 'tienda/productos.html', context)


def contacto(request):
    return render(request, 'tienda/contactanos.html')


def cliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    context = {'cliente': cliente}
    return render(request, 'tienda/Clientes.html', context)


def crearCliente(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'tienda/clienteF.html', context)

def actualizarCliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    form = ClienteForm(instance=cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'tienda/clienteF.html', context)


def borrarCliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == "POST":
        cliente.delete()
    context = {'item': cliente}
    return render(request, 'tienda/borrar.html', context)

