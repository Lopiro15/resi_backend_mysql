from rest_framework import viewsets
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import requests

from proprio.models import *
from proprio.serializers import *

from django_filters import rest_framework as filters

class ResiFilter(filters.FilterSet):
    class Meta:
        model = Residence

        fields = {
            'prixjournalier': ['iexact', 'lte', 'gte'],
            'idproprio__id': ['iexact'],
            'ville': ['icontains'],
            'quartier': ['icontains'],
            'disponibilite': ['iexact'],
            'nbpieces' : ['iexact'],
        }


# Create your views here.
class ProprioViewSet(viewsets.ModelViewSet):
    queryset = Proprietaire.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ProprietaireSerializer
    
    

class ResiViewSet(viewsets.ModelViewSet):
    queryset = Residence.objects.all()
    serializer_class = Resiserializer
    permission_classes = (IsAuthenticated, )
    filter_class = ResiFilter
    
class PiecesResiViewSet(viewsets.ModelViewSet):
    queryset = Piecesresi.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = PiecesResiserializer
    filterset_fields = ['idresidence__id']

class ImagePieceResiViewSet(viewsets.ModelViewSet):
    queryset = Imagepieceresi.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ImagePieceResiserializer
    filterset_fields = ['idpiece__id']

class HistoriqueViewSet(viewsets.ModelViewSet):
    queryset = Historiqueresi.objects.all()
    serializer_class = HistoriqueSerializer
    permission_classes = (IsAuthenticated, )
    filterset_fields = ['idclient__id', 'idresidence__id']
    
