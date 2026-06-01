from rest_framework import viewsets

from .models import (
    Contenido,
    Leccion,
    ModuloEducativo,
    ProgresoEducativo,
    ProgresoLeccion,
)
from .serializers import (
    ContenidoSerializer,
    LeccionSerializer,
    ModuloEducativoSerializer,
    ProgresoEducativoSerializer,
    ProgresoLeccionSerializer,
)


class ModuloEducativoViewSet(viewsets.ModelViewSet):
    queryset = ModuloEducativo.objects.all()
    serializer_class = ModuloEducativoSerializer


class ContenidoViewSet(viewsets.ModelViewSet):
    queryset = Contenido.objects.all()
    serializer_class = ContenidoSerializer


class LeccionViewSet(viewsets.ModelViewSet):
    queryset = Leccion.objects.all()
    serializer_class = LeccionSerializer


class ProgresoEducativoViewSet(viewsets.ModelViewSet):
    queryset = ProgresoEducativo.objects.all()
    serializer_class = ProgresoEducativoSerializer


class ProgresoLeccionViewSet(viewsets.ModelViewSet):
    queryset = ProgresoLeccion.objects.all()
    serializer_class = ProgresoLeccionSerializer
