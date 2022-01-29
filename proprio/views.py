from rest_framework import viewsets
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from proprio.models import Imageresi, Proprietaire, Residence, Historiqueresi
from proprio.serializers import ImageResiserializer, ProprietaireSerializer, Resiserializer, HistoriqueSerializer

from django_filters import rest_framework as filters

class ResiFilter(filters.FilterSet):
    class Meta:
        model = Residence

        fields = {
            'prix': ['iexact', 'lte', 'gte'],
            'idproprio': ['iexact'],
            'ville': ['icontains'],
            'quartier': ['icontains'],
            'disponibilité': ['iexact'],
            }


# Create your views here.
class ProprioViewSet(viewsets.ModelViewSet):
    queryset = Proprietaire.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ProprietaireSerializer
    
    def create(self, request, *args, **kwargs):
        if not request.POST._mutable:
            request.POST._mutable = True
        request.POST['password'] = make_password(request.POST['password'], salt=None, hasher='default')
        serializer = ProprietaireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, *args, **kwargs):
        try:
            proprio = Proprietaire.objects.get(pk=kwargs.get('pk'))
        except Proprietaire.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if not request.POST._mutable:
            request.POST._mutable = True
        request.POST['password'] = make_password(request.POST['password'], salt=None, hasher='default')
        
        serializer = ProprietaireSerializer(proprio, data=request.POST, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResiViewSet(viewsets.ModelViewSet):
    queryset = Residence.objects.all()
    serializer_class = Resiserializer
    permission_classes = (IsAuthenticated, )
    filter_class = ResiFilter
    
class ImageResiViewSet(viewsets.ModelViewSet):
    queryset = Imageresi.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ImageResiserializer

class HistoriqueViewSet(viewsets.ModelViewSet):
    queryset = Historiqueresi.objects.all()
    serializer_class = HistoriqueSerializer
    permission_classes = (IsAuthenticated, )
    filterset_fields = ['idclient', 'idresidence']
    
