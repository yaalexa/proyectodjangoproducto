from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from drf_yasg.utils import swagger_auto_schema

from roles.models import Rol
from .models import Perfil

from .serializer import RegistroSerializer, LoginSerializer


class RegistroView(APIView):

    @swagger_auto_schema(
        request_body=RegistroSerializer
    )
    def post(self, request):

        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        rol_id = request.data.get("rol")

        if User.objects.filter(
            username=username
        ).exists():

            return Response({
                "mensaje": "El usuario ya existe"
            }, status=400)

        try:

            rol = Rol.objects.get(
                id=rol_id
            )

        except Rol.DoesNotExist:

            return Response({
                "mensaje": "El rol no existe"
            }, status=400)

        usuario = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        Perfil.objects.create(
            usuario=usuario,
            rol=rol
        )

        token = Token.objects.create(
            user=usuario
        )

        return Response({

            "mensaje": "Usuario registrado correctamente",

            "token": token.key,

            "usuario": usuario.username,

            "rol": rol.nombre

        })


class LoginView(APIView):

    @swagger_auto_schema(
        request_body=LoginSerializer
    )
    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        usuario = authenticate(
            username=username,
            password=password
        )

        if usuario:

            token, creado = Token.objects.get_or_create(
                user=usuario
            )

            perfil = Perfil.objects.get(
                usuario=usuario
            )

            return Response({

                "mensaje": "Login correcto",

                "token": token.key,

                "usuario": usuario.username,

                "rol": perfil.rol.nombre

            })

        return Response({

            "mensaje": "Usuario o contraseña incorrectos"

        }, status=401)