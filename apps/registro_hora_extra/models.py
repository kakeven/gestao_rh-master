from django.db import models
from apps.funcionarios.models import Funcionarios


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.PROTECT)


    def __str__(self):
        return self.motivo
