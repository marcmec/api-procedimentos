from rest_framework import generics
from django.db.models import Sum, F
from rest_framework.response import Response
from .models import Pedido, Procedimento
from .serializers import AtendimentoSerializer, PedidoSerializer


class PedidoList(generics.ListCreateAPIView):

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def get(self, request):
        transacao = Procedimento.objects.all()
        serializer = AtendimentoSerializer(transacao, many=True)
        total_pedido = transacao.aggregate(
            Sum('valor_procedimento'))
        comissao = 0
        for chave, valor in total_pedido.items():
            total_pedido[chave] = float(valor)
            comissao = round(total_pedido[chave]*0.01, 3)
        return Response({'total': total_pedido if total_pedido else 0, 'comissao': comissao, 'pedido': serializer.data})


class Pedidos(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class ProcedimentosList(generics.ListCreateAPIView):
    queryset = Procedimento.objects.all()
    serializer_class = AtendimentoSerializer
