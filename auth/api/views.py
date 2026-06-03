from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import (
    AuditoriaLogin,
    Credencial,
    Rol,
    TipoDocumento,
    Usuario,
    UsuarioRol
)
from .serializers import (
    AuditoriaLoginSerializer,
    CredencialSerializers,
    RolSerializer,
    TipoDocumentoSerializers,  
    UsuarioSerializers,
    UsuarioRolSerializers
)

class auditoria_loginViewSet(viewsets.ModelViewSet):
    queryset = AuditoriaLogin.objects.all()
    serializer_class = AuditoriaLoginSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['id_auditoria', 'tipo_evento', 'fecha_evento', 'estado_evento']
    ordering = ['id_auditoria']
    filterset_fields = ['tipo_evento', 'estado_evento']
    search_fields = ['tipo_evento', 'estado_evento', 'ip_address']
    
class credencialViewSet(viewsets.ModelViewSet):
    queryset = Credencial.objects.all()
    serializer_class = CredencialSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['id_credencial', 'fecha_creacion', 'fecha_modificacion']
    ordering = ['id_credencial']
    filterset_fields = ['activo', 'requiere_cambio']
    search_fields = ['algoritmo']
    
class rolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['id_rol', 'nombre_rol', 'fecha_creacion', 'fecha_modificacion']
    ordering = ['id_rol']
    filterset_fields = ['activo']
    search_fields = ['nombre_rol', 'descripcion']
    
class tipo_documentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['id_tipo_documento', 'nombre', 'codigo', 'fecha_creacion']
    ordering = ['id_tipo_documento']
    filterset_fields = ['activo']
    search_fields = ['nombre', 'codigo']
    
class usuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['id_usuario', 'nombre', 'apellido', 'email', 'fecha_creacion', 'fecha_registro']
    ordering = ['id_usuario']
    filterset_fields = ['activo', 'estado', 'ciudad']
    search_fields = ['nombre', 'apellido', 'email', 'cedula']
    
class usuario_rolViewSet(viewsets.ModelViewSet):
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['id_usuario_rol', 'fecha_asignacion', 'fecha_creacion']
    ordering = ['id_usuario_rol']
    filterset_fields = ['activo']
    search_fields = []
    
