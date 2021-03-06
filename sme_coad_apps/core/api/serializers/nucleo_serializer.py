from rest_framework import serializers

from ..serializers.divisao_serializer import DivisaoLookUpSerializer
from ...models import Nucleo
from ....users.api.serializers.usuario_serializer import UsuarioLookUpSerializer


class NucleoSerializer(serializers.ModelSerializer):
    divisao = DivisaoLookUpSerializer()
    chefe = UsuarioLookUpSerializer()
    suplente_chefe = UsuarioLookUpSerializer()

    class Meta:
        model = Nucleo
        fields = ('id', 'sigla', 'nome', 'chefe', 'suplente_chefe', 'divisao', 'uuid')


class NucleoLookUpSerializer(serializers.ModelSerializer):
    divisao = DivisaoLookUpSerializer()

    class Meta:
        model = Nucleo
        fields = ('sigla', 'uuid', 'divisao')


class NucleoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nucleo
        fields = ('id', 'sigla', 'nome', 'chefe', 'suplente_chefe', 'divisao', 'uuid')
