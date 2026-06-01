from rest_framework import serializers
from .models import (
    auditoria_login,
    credencial,
    rol,
    tipo_documento,
    usuario,
    usuario_rol
)

class AuditoriaLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = auditoria_login
        fields = '__all__'
        
class CredencialSerializers(serializers.ModelSerializer):
    class Meta:
        model = credencial
        fields = '__all__'
        
        
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = rol
        fields = '__all__'
    
class Tipo_DocumentoSerializers(serializers.ModelSerializers):
    class Meta:
        model = tipo_documento
        fields = '__all__'
        
class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = usuario 
        fields = '__all__'
        
class Usuario_RolSerializers(serializers.ModelSerializers):
    class Meta:
        model = usuario_rol
        fields = '__all__'
        
        