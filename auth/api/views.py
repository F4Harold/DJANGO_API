from django.shortcuts import render
from rest_framework import viewsets
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
    Tipo_DocumentoSerializers,
    UsuarioSerializers,
    Usuario_RolSerializers
)

class auditoria_loginViewSet(viewsets.ModelViewSet):
    queryset = AuditoriaLogin.objects.all()
    serializer_class = AuditoriaLoginSerializer
    
class credencialViewSet(viewsets.ModelViewSet):
    queryset = Credencial.objects.all()
    serializer_class = CredencialSerializers
    
class rolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    
class tipo_documentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = Tipo_DocumentoSerializers
    
class usuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers
    
class usuario_rolViewSet(viewsets.ModelViewSet):
    queryset = UsuarioRol.objects.all()
    serializer_class = Usuario_RolSerializers
    
