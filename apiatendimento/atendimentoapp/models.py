from django.db import models


class Procedimento(models.Model):
    procedimento = models.CharField(max_length=10)
    valor_procedimento = models.FloatField()

    class Meta:
        ordering = ['procedimento']

    def __str__(self):
        return self.procedimento


class Pedido(models.Model):
    nome_atendente = models.CharField(max_length=30, default='atendente')
    resumo_pedido = models.ManyToManyField(
        Procedimento)

    class Meta:

        db_table = 'pedido'

    def __str__(self):
        return self.nome_atendente
