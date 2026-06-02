from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .models import (
    Banco, ProductoCrediticio, AsesorBancario,
    ContactoAsesor, Lead, ConversacionUsuarioAsesor,
    CreditoDesembolsado, TransaccionComision,
)
from .serializers import (
    BancoSerializer, ProductoCrediticioSerializer, AsesorBancarioSerializer,
    ContactoAsesorSerializer, LeadSerializer, ConversacionUsuarioAsesorSerializer,
    CreditoDesembolsadoSerializer, TransaccionComisionSerializer,
)

class BancoViewSet(viewsets.ModelViewSet):
    queryset            = Banco.objects.filter(activo=True)
    serializer_class    = BancoSerializer
    filter_backends     = [OrderingFilter]
    ordering_fields     = ['nombre_banco', 'ciudad', 'fecha_creacion']
    ordering            = ['nombre_banco']   # orden por defecto

class ProductoCrediticioViewSet(viewsets.ModelViewSet):
    queryset            = ProductoCrediticio.objects.filter(activo=True)
    serializer_class    = ProductoCrediticioSerializer
    filter_backends     = [OrderingFilter]
    ordering_fields     = ['nombre_producto', 'monto_minimo', 'tasa_minima', 'fecha_creacion']
    ordering            = ['nombre_producto']

class AsesorBancarioViewSet(viewsets.ModelViewSet):
    queryset            = AsesorBancario.objects.filter(activo=True)
    serializer_class    = AsesorBancarioSerializer
    filter_backends     = [OrderingFilter]
    ordering_fields     = ['nombre', 'apellido', 'especialidad', 'fecha_creacion']
    ordering            = ['nombre']

class ContactoAsesorViewSet(viewsets.ModelViewSet):
    queryset            = ContactoAsesor.objects.filter(activo=True)
    serializer_class    = ContactoAsesorSerializer
    filter_backends     = [OrderingFilter]
    ordering_fields     = ['disponible_desde', 'fecha_creacion']
    ordering            = ['id_contacto']

class LeadViewSet(viewsets.ModelViewSet):
    queryset            = Lead.objects.filter(activo=True)
    serializer_class    = LeadSerializer
    filter_backends     = [OrderingFilter]
    ordering_fields     = ['estado_lead', 'monto_interes', 'fecha_generacion', 'fecha_creacion']
    ordering            = ['-fecha_generacion']

class ConversacionUsuarioAsesorViewSet(viewsets.ModelViewSet):
    queryset            = ConversacionUsuarioAsesor.objects.filter(activo=True)
    serializer_class    = ConversacionUsuarioAsesorSerializer
    filter_backends     = [OrderingFilter]
    ordering_fields     = ['tipo_contacto', 'fecha_mensaje', 'fecha_creacion']
    ordering            = ['-fecha_mensaje']

class CreditoDesembolsadoViewSet(viewsets.ModelViewSet):
    queryset            = CreditoDesembolsado.objects.filter(activo=True)
    serializer_class    = CreditoDesembolsadoSerializer
    filter_backends     = [OrderingFilter]
    ordering_fields     = ['estado_credito', 'monto_aprobado', 'fecha_desembolso', 'fecha_creacion']
    ordering            = ['-fecha_desembolso']

class TransaccionComisionViewSet(viewsets.ModelViewSet):
    queryset            = TransaccionComision.objects.filter(activo=True)
    serializer_class    = TransaccionComisionSerializer
    filter_backends     = [OrderingFilter]
    ordering_fields     = ['estado', 'monto_comision', 'fecha_transaccion', 'fecha_creacion']
    ordering            = ['-fecha_transaccion']