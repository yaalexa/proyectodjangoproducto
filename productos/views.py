from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from .models import Producto
from .serializer import ProductoEntrada


class ProductosView(APIView):

    permission_classes = [IsAuthenticated]

    # LISTAR TODOS O BUSCAR POR ID
    def get(self, request, id=None):

        if id:
            producto = Producto.objects.get(id=id)

            return Response({
                "id": producto.id,
                "nombre": producto.nombre,
                "descripcion": producto.descripcion,
                "precio": producto.precio,
                "stock": producto.stock
            })

        productos = Producto.objects.all()

        lista = []

        for producto in productos:
            lista.append({
                "id": producto.id,
                "nombre": producto.nombre,
                "descripcion": producto.descripcion,
                "precio": producto.precio,
                "stock": producto.stock
            })

        return Response(lista)


    # GUARDAR
    @swagger_auto_schema(
        operation_description="Guardar producto",
        request_body=ProductoEntrada
    )
    def post(self, request):

        Producto.objects.create(
            nombre=request.data.get("nombre"),
            descripcion=request.data.get("descripcion"),
            precio=request.data.get("precio"),
            stock=request.data.get("stock")
        )

        return Response({
            "mensaje": "Producto guardado correctamente"
        })

class ProductosIdView(APIView):
    # ACTUALIZAR
    @swagger_auto_schema(
        operation_description="Actualizar producto",
        request_body=ProductoEntrada
    )
    def put(self, request, id):

        producto = Producto.objects.get(id=id)

        producto.nombre = request.data.get("nombre")
        producto.descripcion = request.data.get("descripcion")
        producto.precio = request.data.get("precio")
        producto.stock = request.data.get("stock")

        producto.save()

        return Response({
            "mensaje": "Producto actualizado correctamente"
        })


    # ELIMINAR
    def delete(self, request, id):

        producto = Producto.objects.get(id=id)

        producto.delete()

        return Response({
            "mensaje": "Producto eliminado correctamente"
        })