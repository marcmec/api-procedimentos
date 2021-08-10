from rest_framework import serializers
from .models import Atendimento
from django.db.models import Sum


class AtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendimento
        fields = '__all__'
