from rest_framework import serializers

from eventos.models import Cliente, Tipo


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'pago', 'direccion', 'tipo']


class TipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo
        fields = ['nombre_evento']

