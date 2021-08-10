from rest_framework import serializers
from .models import Procedimento, Pedido


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('id', 'resumo_pedido')


class AtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimento
        fields = '__all__'
