from tienda.models import Producto, Marca
from rest_framework import serializers


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'


