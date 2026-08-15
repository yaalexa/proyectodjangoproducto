from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from drf_yasg.utils import swagger_auto_schema

from .serializer import RegistroSerializer, LoginSerializer


class RegistroView(APIView):

    @swagger_auto_schema(
        request_body=RegistroSerializer
    )
    def post(self, request):

        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if User.objects.filter(username=username).exists():
            return Response({
                "mensaje": "El usuario ya existe"
            })

        usuario = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        token = Token.objects.create(user=usuario)

        return Response({
            "mensaje": "Usuario registrado correctamente",
            "token": token.key
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

            return Response({
                "mensaje": "Login correcto",
                "token": token.key
            })

        return Response({
            "mensaje": "Usuario o contraseña incorrectos"
        })