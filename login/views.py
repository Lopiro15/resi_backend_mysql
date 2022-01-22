from proprio.models import Proprietaire
from proprio.serializers import ProprietaireSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from django.db import connection
from rest_framework.permissions import IsAuthenticated


from client.models import Client
from client.serializers import ClientSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    context = {
        'admin' : '/admin/',
        'client' : '/client/',
        'login_client' : '/login/client/',
        'login_proprietaire' : '/login/proprio/',
        'proprietaire' : '/proprio/',
        'residenceetmoyenne' : '/moyenneresi/',
    }
    return Response(context)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def client_login(request, format=None):
    permission_classes = (IsAuthenticated, )
    try:
        client = Client.objects.get(username__exact=request.data['username'])
    except Client.DoesNotExist:
        return Response({"error": "username does not exist", "echec": True} ,status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        if check_password(request.data['password'], client.password):
            return Response(ClientSerializer(client).data, status=status.HTTP_201_CREATED)
        return Response({"error": "password is wrong", "echec": True},status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def proprio_login(request, format=None):
    try:
        proprio = Proprietaire.objects.get(username__exact=request.data['username'])
    except Proprietaire.DoesNotExist:
        return Response({"error": "username does not exist", "echec": True} ,status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        if check_password(request.data['password'], proprio.password):
            return Response(ProprietaireSerializer(proprio).data, status=status.HTTP_201_CREATED)
        return Response({"error": "password is wrong", "echec": True},status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def resi_note(request, format=None):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            sql = "SELECT proprio_residence.*, COUNT(client_noteresidence.note) as nbvote, AVG(client_noteresidence.note) as moyenne FROM proprio_residence, client_noteresidence WHERE proprio_residence.id = client_noteresidence.idresidence GROUP BY client_noteresidence.idresidence ORDER BY moyenne;"
            cursor.execute(sql)
            rows = cursor.fetchall()
            json_data = []
            for obj in rows:
                json_data.append({"idresidence" : obj[0], "idproprio" : obj[1], "description" : obj[2], "ville" : obj[3], "quartier" : obj[4], "prix" : obj[5], "disponibilité" : obj[6], "photocouverture" : obj[7], "nbvote" : obj[8], "moyenne" : obj[9]})
        return Response(json_data, status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        with connection.cursor() as cursor:
            sql = "SELECT proprio_residence.*, COUNT(client_noteresidence.note) as nbvote, AVG(client_noteresidence.note) as moyenne FROM proprio_residence, client_noteresidence WHERE proprio_residence.id = client_noteresidence.idresidence AND proprio_residence.disponibilité = 1 AND proprio_residence.ville LIKE %(v)s AND proprio_residence.quartier LIKE %(q)s AND proprio_residence.prix <= %(p_lte)s AND proprio_residence.prix >= %(p_gte)s GROUP BY client_noteresidence.idresidence ORDER BY moyenne;"
            ville = "%" + request.POST['ville'] + "%"
            quartier = "%" + request.POST['quartier'] + "%"
            param = {'v': ville, 'q': quartier, 'p_lte': request.POST['prix_lte'], 'p_gte': request.POST['prix_gte']}
            cursor.execute(sql, params=param)
            rows = cursor.fetchall()
            json_data = []
            for obj in rows:
                json_data.append({"idresidence" : obj[0], "idproprio" : obj[1], "description" : obj[2], "ville" : obj[3], "quartier" : obj[4], "prix" : obj[5], "disponibilité" : obj[6], "photocouverture" : obj[7], "nbvote" : obj[8], "moyenne" : obj[9]})
        return Response(json_data, status=status.HTTP_201_CREATED)