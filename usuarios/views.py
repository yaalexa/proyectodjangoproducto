from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class RegistroView(APIView):

    def post(self, request):

        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        usuario = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        token = Token.objects.create(user=usuario)

        return Response({
            "mensaje": "Usuario registrado",
            "token": token.key
        })


class LoginView(APIView):

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