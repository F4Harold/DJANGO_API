from django.shortcuts import render

from rest_framework import viewsets

from .models import (
    EstadoPqr,
    Pqr,
    Adjunto,
    RegistroActividad
)

from .serializers import (
    EstadoPqrSerializer,
    PqrSerializer,
    AdjuntoSerializer,
    RegistroActividadSerializer
)

# crud para estado_pqr (GET, POST, PUT, DELETE)
class EstadoPqrViewSet(viewsets.ModelViewSet):
    queryset = EstadoPqr.objects.all()
    serializer_class = EstadoPqrSerializer

# crud para pqr
class PqrViewSet(viewsets.ModelViewSet):
    queryset = Pqr.objects.all()
    serializer_class = PqrSerializer

# crud para adjunto
class AdjuntoViewSet(viewsets.ModelViewSet):
    queryset = Adjunto.objects.all()
    serializer_class = AdjuntoSerializer

# crud para registro_actividad
class RegistroActividadViewSet(viewsets.ModelViewSet):
    queryset = RegistroActividad.objects.all()
    serializer_class = RegistroActividadSerializer