from rest_framework import filters, viewsets

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
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'id_estado',
        'nombre',
        'descripcion',
        'activo',
        'fecha_creacion',
        'fecha_modificacion',
    ]
    ordering = ['id_estado']

# crud para pqr
class PqrViewSet(viewsets.ModelViewSet):
    queryset = Pqr.objects.all()
    serializer_class = PqrSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'id_pqr',
        'id_usuario',
        'id_estado',
        'activo',
        'fecha_creacion',
        'fecha_modificacion',
    ]
    ordering = ['id_pqr']

# crud para adjunto
class AdjuntoViewSet(viewsets.ModelViewSet):
    queryset = Adjunto.objects.all()
    serializer_class = AdjuntoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'id_adjunto',
        'id_pqr',
        'nombre_archivo',
        'tipo_mime',
        'tamano_bytes',
        'activo',
        'fecha_creacion',
        'fecha_modificacion',
    ]
    ordering = ['id_adjunto']

# crud para registro_actividad
class RegistroActividadViewSet(viewsets.ModelViewSet):
    queryset = RegistroActividad.objects.all()
    serializer_class = RegistroActividadSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'id_registro',
        'id_usuario',
        'tipo_actividad',
        'entidad_afectada',
        'fecha_actividad',
        'fecha_creacion',
    ]
    ordering = ['id_registro']
