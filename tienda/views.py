from django.shortcuts import render
from .models import *
# Create your views here.


def home (request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda/index.html', context)