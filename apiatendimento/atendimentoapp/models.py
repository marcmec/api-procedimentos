from django.db import models


class Atendimento(models.Model):
    class Meta:

        db_table = 'atendimento'

    pedido = models.CharField(max_length=20)

    def __str__(self):
        return self.pedido
