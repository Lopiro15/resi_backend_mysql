
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import requests

from client.models import AjoutDeSejour, Client, Commande, NoteResidence
from client.serializers import AjoutSerializer, ClientSerializer, CommandeSerializer, NoteSerializer


# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    permission_classes = (IsAuthenticated, )
    filterset_fields = ['idclient', 'idresidence', 'statucommande']
    
class AjoutViewSet(viewsets.ModelViewSet):
    queryset = AjoutDeSejour.objects.all()
    serializer_class = AjoutSerializer
    permission_classes = (IsAuthenticated, )
    filterset_fields = ['idcommande', 'statudemande']
    
class NoteViewSet(viewsets.ModelViewSet):
    queryset = NoteResidence.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated, )
    filterset_fields = ['idclient' ,'idresidence']