from rest_framework import serializers

from .models import (
    EstadoPqr,
    Pqr,
    Adjunto,
    RegistroActividad
)

# Serializador para estado_pqr
class EstadoPqrSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPqr
        fields = '__all__'

# Serializador para pqr
class PqrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pqr
        fields = '__all__'

# Serializador para adjunto
class AdjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adjunto
        fields = '__all__'

# Serializador para registro_actividad
class RegistroActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroActividad
        fields = '__all__'