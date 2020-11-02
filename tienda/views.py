from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'tienda/index.html')


def productos(request):
    return render(request, 'tienda/productos.html')


def contacto(request):
    return render(request, 'tienda/contactanos.html')