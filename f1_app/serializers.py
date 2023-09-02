from rest_framework import serializers
from .models import Equipe, Pilotos

# Definição do serializer PilotosSerializer para Pilotos
class PilotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilotos 
        fields = '__all__' 

# Definição do serializer EquipeSerializer para Equipe
class EquipeSerializer(serializers.ModelSerializer):
    # Adiciona um campo personalizado 'pilotos' ao serializer
    pilotos = serializers.SerializerMethodField()

    class Meta:
        model = Equipe
        fields = '__all__'

    def get_pilotos(self, obj):
        # Obtém todos os pilotos associados a uma equipe específica
        pilotos = Pilotos.objects.filter(equipe=obj)

        # Serializa a lista de pilotos
        pilotos_serializer = PilotosSerializer(pilotos, many=True)

        # Retorna os dados serializados dos pilotos
        return pilotos_serializer.data

