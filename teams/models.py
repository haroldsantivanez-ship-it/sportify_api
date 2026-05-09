from django.db import models

class Equipo(models.Model):
    CATEGORIAS = [
        ('primera', 'Primera División'),
        ('segunda', 'Segunda División'),
        ('tercera', 'Tercera División'),
    ]

    nombre    = models.CharField(max_length=100)
    ciudad    = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='primera')

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    POSICIONES = [
        ('portero', 'Portero'),
        ('defensa', 'Defensa'),
        ('mediocampista', 'Mediocampista'),
        ('delantero', 'Delantero'),
    ]

    nombre          = models.CharField(max_length=100)
    posicion        = models.CharField(max_length=20, choices=POSICIONES)
    numero_camiseta = models.PositiveIntegerField()
    equipo          = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores')

    def __str__(self):
        return f"{self.nombre} - #{self.numero_camiseta}"