from rest_framework import serializers


class RegistroSerializer(serializers.Serializer):

    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    rol = serializers.IntegerField()


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()