from rest_framework import generics
from .models import Atendimento
from .serializers import AtendimentoSerializer


class AtendimentoList(generics.ListCreateAPIView):

    queryset = Atendimento.objects.all()
    serializer_class = AtendimentoSerializer
