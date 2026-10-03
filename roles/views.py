from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import Rol
from .serializer import RolSerializer


class RolesView(APIView):

    def get(self, request):

        roles = Rol.objects.all()

        serializer = RolSerializer(
            roles,
            many=True
        )

        return Response(serializer.data)
    
    @swagger_auto_schema(
        request_body=RolSerializer
    )
    def post(self, request):

        serializer = RolSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({
                "mensaje": "Rol registrado correctamente",
                "rol": serializer.data
            }, status=201)

        return Response(
            serializer.errors,
            status=400
        )