from rest_framework import viewsets

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
from .serializers import (
    CategoriaSerializer,
    EditarMetaSerializer,
    FinanzasSerializer,
    InversionSerializer,
    MetaSerializer,
    MovimientoIngresoEgresoSerializer,
    MovimientoInversionSerializer,
    MovimientoMetaSerializer,
    NivelRiesgoSerializer,
    TipoIngresoInversionSerializer,
    TipoIngresoMetaSerializer,
    TipoIngresoSerializer,
    TipoInversionSerializer,
)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class MovimientoIngresoEgresoViewSet(viewsets.ModelViewSet):
    queryset = MovimientoIngresoEgreso.objects.all()
    serializer_class = MovimientoIngresoEgresoSerializer


class TipoIngresoViewSet(viewsets.ModelViewSet):
    queryset = TipoIngreso.objects.all()
    serializer_class = TipoIngresoSerializer


class FinanzasViewSet(viewsets.ModelViewSet):
    queryset = Finanzas.objects.all()
    serializer_class = FinanzasSerializer


class TipoInversionViewSet(viewsets.ModelViewSet):
    queryset = TipoInversion.objects.all()
    serializer_class = TipoInversionSerializer


class NivelRiesgoViewSet(viewsets.ModelViewSet):
    queryset = NivelRiesgo.objects.all()
    serializer_class = NivelRiesgoSerializer


class MovimientoInversionViewSet(viewsets.ModelViewSet):
    queryset = MovimientoInversion.objects.all()
    serializer_class = MovimientoInversionSerializer


class TipoIngresoInversionViewSet(viewsets.ModelViewSet):
    queryset = TipoIngresoInversion.objects.all()
    serializer_class = TipoIngresoInversionSerializer


class InversionViewSet(viewsets.ModelViewSet):
    queryset = Inversion.objects.all()
    serializer_class = InversionSerializer


class EditarMetaViewSet(viewsets.ModelViewSet):
    queryset = EditarMeta.objects.all()
    serializer_class = EditarMetaSerializer


class MovimientoMetaViewSet(viewsets.ModelViewSet):
    queryset = MovimientoMeta.objects.all()
    serializer_class = MovimientoMetaSerializer


class TipoIngresoMetaViewSet(viewsets.ModelViewSet):
    queryset = TipoIngresoMeta.objects.all()
    serializer_class = TipoIngresoMetaSerializer


class MetaViewSet(viewsets.ModelViewSet):
    queryset = Meta.objects.all()
    serializer_class = MetaSerializer
