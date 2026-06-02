from rest_framework import serializers
from .models import (
    AuditoriaLogin,
    Credencial,
    Rol,
    TipoDocumento,
    Usuario,
    UsuarioRol
)

class AuditoriaLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaLogin  # ← mayúscula
        fields = '__all__'

class CredencialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Credencial  # ← mayúscula
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol  # ← mayúscula
        fields = '__all__'

class TipoDocumentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento  # ← mayúscula
        fields = '__all__'

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario  # ← mayúscula
        fields = '__all__'

class UsuarioRolSerializers(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRol  # ← mayúscula
        fields = '__all__'