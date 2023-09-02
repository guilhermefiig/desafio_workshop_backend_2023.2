from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .models import Equipe, Pilotos
from .serializers import EquipeSerializer, PilotosSerializer

# Viewset para o modelo Equipe
class EquipeViewset(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    pagination_class = LimitOffsetPagination # Define a paginação usando LimitOffsetPagination

# Viewset para o modelo Pilotos
class PilotosViewset(viewsets.ModelViewSet):
    queryset = Pilotos.objects.all()  
    serializer_class = PilotosSerializer 
    pagination_class = LimitOffsetPagination  # Define a paginação usando LimitOffsetPagination

