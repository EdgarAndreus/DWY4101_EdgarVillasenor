from django.shortcuts import render
from .models import *
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


def home(request):
    return render(request, 'tienda/index.html')


def productos(request):
    producto = Producto.objects.all()
    return render(request, 'tienda/productos.html', {'producto': producto})


def contacto(request):
    return render(request, 'tienda/contactanos.html')

class CrearProducto(CreateView):
    model = Producto
    fields = '__all__'
    initial={'descripcion':'ninguna',}


class ModificarProducto(UpdateView):
    model = Producto
    fields = ['nombre','codigo','marca','precio','descripcion']


class BorrarProducto(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos')


class VistaProducto(generic.DetailView):
    model = Producto

