from rest_framework import serializers

from .models import (
    Contenido,
    Leccion,
    ModuloEducativo,
    ProgresoEducativo,
    ProgresoLeccion,
)


class ModuloEducativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuloEducativo
        fields = "__all__"


class ContenidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenido
        fields = "__all__"


class LeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = "__all__"


class ProgresoEducativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoEducativo
        fields = "__all__"


class ProgresoLeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoLeccion
        fields = "__all__"
