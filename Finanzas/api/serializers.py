from rest_framework import serializers

from .models import (
    Categoria,
    EditarMeta,
    Finanzas,
    Inversion,
    Meta,
    MovimientoIngresoEgreso,
    MovimientoInversion,
    MovimientoMeta,
    NivelRiesgo,
    TipoIngreso,
    TipoIngresoInversion,
    TipoIngresoMeta,
    TipoInversion,
)


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class MovimientoIngresoEgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoIngresoEgreso
        fields = "__all__"


class TipoIngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIngreso
        fields = "__all__"


class FinanzasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finanzas
        fields = "__all__"


class TipoInversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInversion
        fields = "__all__"


class NivelRiesgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelRiesgo
        fields = "__all__"


class MovimientoInversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoInversion
        fields = "__all__"


class TipoIngresoInversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIngresoInversion
        fields = "__all__"


class InversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inversion
        fields = "__all__"


class EditarMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditarMeta
        fields = "__all__"


class MovimientoMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoMeta
        fields = "__all__"


class TipoIngresoMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIngresoMeta
        fields = "__all__"


class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meta
        fields = "__all__"
