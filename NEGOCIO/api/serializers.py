from rest_framework import serializers
from .models import (
    Banco,
    ProductoCrediticio,
    AsesorBancario,
    ContactoAsesor,
    Lead,
    ConversacionUsuarioAsesor,
    CreditoDesembolsado,
    TransaccionComision,
)

# Serializador para Banco
class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = '__all__'

# Serializador para ProductoCrediticio
class ProductoCrediticioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoCrediticio
        fields = '__all__'

# Serializador para AsesorBancario
class AsesorBancarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsesorBancario
        fields = '__all__'

# Serializador para ContactoAsesor
class ContactoAsesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactoAsesor
        fields = '__all__'

# Serializador para Lead
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

# Serializador para ConversacionUsuarioAsesor
class ConversacionUsuarioAsesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversacionUsuarioAsesor
        fields = '__all__'

# Serializador para CreditoDesembolsado
class CreditoDesembolsadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditoDesembolsado
        fields = '__all__'

# Serializador para TransaccionComision
class TransaccionComisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionComision
        fields = '__all__'