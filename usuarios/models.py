from django.db import models
from django.contrib.auth.models import User
from roles.models import Rol


class Perfil(models.Model):

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    rol = models.ForeignKey(
        Rol,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.usuario.username