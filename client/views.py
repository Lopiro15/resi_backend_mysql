
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from client.models import AjoutDeSejour, Client, Commande, NoteResidence
from client.serializers import AjoutSerializer, ClientSerializer, CommandeSerializer, NoteSerializer


# Create your views here.
class ClienViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )
    
    def create(self, request, *args, **kwargs):
        if not request.POST._mutable:
            request.POST._mutable = True
        request.POST['password'] = make_password(request.POST['password'], salt=None, hasher='default')
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        try:
            client = Client.objects.get(pk=kwargs.get('pk'))
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if not request.POST._mutable:
            request.POST._mutable = True
        request.POST['password'] = make_password(request.POST['password'], salt=None, hasher='default')
        
        serializer = ClientSerializer(client, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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