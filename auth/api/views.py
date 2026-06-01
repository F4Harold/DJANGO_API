from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    auditoria_login,
    credencial,
    rol,
    tipo_documento,
    usuario,
    usuario_rol
)
from .serializers import (
    auditoria_loginSerializer,
    credencialSerializers,
    rolSerializer,
    tipo_documentoSerializers,
    usuarioSerializers,
    usuario_rolSerializers
)

class auditoria_loginViewSet(viewsets.ModelViewSet):
    queryset = auditoria_login.objects.all()
    serializer_class = auditoria_loginSerializer
    
class credencialViewSet(viewsets.ModelViewSet):
    queryset = credencial.objects.all()
    serializer_class = credencialSerializers
    
class rolViewSet(viewsets.ModelViewSet):
    queryset = rol.objects.all()
    serializer_class = rolSerializer
    
class tipo_documentoViewSet(viewsets.ModelViewSet):
    queryset = tipo_documento.objects.all()
    serializer_class = tipo_documentoSerializers
    
class usuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializers
    
class usuario_rolViewSet(viewsets.ModelViewSet):
    queryset = usuario_rol.objects.all()
    serializer_class = usuario_rolSerializers
    
