from django.shortcuts import render
from tienda.models import Producto, Marca
from rest_framework import viewsets, permissions
from quick.serializers import ProductoSerializer, MarcaSerializer
# Create your views here.


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [permissions.IsAuthenticated]



