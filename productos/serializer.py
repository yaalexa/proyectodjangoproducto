from rest_framework import serializers

class ProductoEntrada(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)
    descripcion = serializers.CharField(max_length=200)
    precio = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock = serializers.IntegerField()


class ProductoSalida(serializers.Serializer):
    mensaje = serializers.CharField(max_length=100)