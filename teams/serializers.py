from rest_framework import serializers
from .models import Equipo, Jugador


class JugadorSerializer(serializers.ModelSerializer):
    equipo_nombre = serializers.CharField(source='equipo.nombre', read_only=True)

    class Meta:
        model  = Jugador
        fields = ['id', 'nombre', 'posicion', 'numero_camiseta', 'equipo', 'equipo_nombre']


class EquipoSerializer(serializers.ModelSerializer):
    total_jugadores = serializers.SerializerMethodField()
    jugadores       = JugadorSerializer(many=True, read_only=True)

    class Meta:
        model  = Equipo
        fields = ['id', 'nombre', 'ciudad', 'categoria', 'total_jugadores', 'jugadores']

    def get_total_jugadores(self, obj):
        return obj.jugadores.count()