from proprio.models import Proprietaire
from proprio.serializers import ProprietaireSerializer
from .serializers import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password, make_password
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
        'change_password_client' : '/password/client/',
        'change_password_proprietaire' : '/password/proprio/',
        'proprietaire' : '/proprio/',
        'residenceetmoyenne' : '/moyenneresi/',
        'historiquevisitemoyenne' : '/historiquemoyenresi/',
        'disponibiliteresi' : '/disponibiliteresi/',
        'documentation' : '/swagger/',
    }
    return Response(context)




@swagger_auto_schema(method='post', request_body=LoginClientSerializer, responses={201: ClientSerializer})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def client_login(request, format=None):
    try:
        client = Client.objects.get(username__exact=request.data['username'])
    except Client.DoesNotExist:
        return Response({"error": "username does not exist", "echec": True} ,status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        if check_password(request.data['password'], client.password):
            return Response(ClientSerializer(client).data, status=status.HTTP_201_CREATED)
        return Response({"error": "password is wrong", "echec": True},status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(method='post', request_body=PasswordchangeSerializer, responses={201: PasswordchangeresultSerializer, 404: PasswordchangeresultSerializer})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def client_change_password(request, format=None):
    try:
        client = Client.objects.get(username__exact=request.data['username'])
    except Client.DoesNotExist:
        return Response({"msg": "username does not exist", "success": False} ,status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        if check_password(request.data['password'], client.password):
            data = {"password": make_password(request.data['newpassword'], salt=None, hasher='default')}
            serializer = ClientSerializer(client, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "password changed", "success": True}, status=status.HTTP_201_CREATED)
        return Response({"msg": "password is wrong", "success": False},status=status.HTTP_404_NOT_FOUND)



@swagger_auto_schema(method='post', request_body=LoginClientSerializer, responses={201: ProprietaireSerializer})
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
    
@swagger_auto_schema(method='post', request_body=PasswordchangeSerializer, responses={201: PasswordchangeresultSerializer, 404: PasswordchangeresultSerializer})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def proprio_change_password(request, format=None):
    try:
        proprio = Proprietaire.objects.get(username__exact=request.data['username'])
    except Proprietaire.DoesNotExist:
        return Response({"msg": "username does not exist", "success": False} ,status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        if check_password(request.data['password'], proprio.password):
            data = {"password": make_password(request.data['newpassword'], salt=None, hasher='default')}
            serializer = ProprietaireSerializer(proprio, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "password changed", "success": True}, status=status.HTTP_201_CREATED)
        return Response({"msg": "password is wrong", "success": False},status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(method='get', responses={201: MoyenneResiSerializer})
@swagger_auto_schema(method='post', request_body=MoyenneSerializer, responses={201: MoyenneResiSerializer})
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


@swagger_auto_schema(method='get', responses={201: Historiquemoyenresi})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def historique_annonce(request, Format=None):
    with connection.cursor() as cursor:
        sql1 = "CREATE VIEW IF NOT EXISTS annonce3D AS SELECT idresidence, COUNT(tempssurannonce) as nbvisite3D FROM proprio_historiqueresi WHERE  visite3D = 1 GROUP BY idresidence"
        cursor.execute(sql1)
        sql2 = "CREATE VIEW IF NOT EXISTS annoncecommande AS SELECT idresidence, COUNT(tempssurannonce) as nbcommande FROM proprio_historiqueresi WHERE residencecommandé = 1 GROUP BY idresidence"
        cursor.execute(sql2)
        json_data = []
        sql= "SELECT proprio_historiqueresi.idresidence, annonce3D.nbvisite3D, annoncecommande.nbcommande, COUNT(tempssurannonce) as nbvisite, AVG(tempssurannonce) as moyenne FROM proprio_historiqueresi, annonce3D, annoncecommande WHERE proprio_historiqueresi.idresidence = annonce3D.idresidence AND proprio_historiqueresi.idresidence = annoncecommande.idresidence GROUP BY proprio_historiqueresi.idresidence ORDER BY moyenne"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            json_data.append({"idresidence" : row[0], "nbvisite3D" : row[1], "nbcommandeissu" : row[2], "nbvisitetotal" : row[3], "moyennetemps" : row[4]})
    return Response(json_data, status=status.HTTP_201_CREATED)
     

@swagger_auto_schema(method='post', request_body=DisporesiSerializer, responses={201: DisporesiresultSerializer})   
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def disponibilite_resi(request, Format=None):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            sql = "SELECT * FROM client_commande WHERE idresidence = %(id)s AND datedebut <= %(fin)s AND datefin >= %(deb)s"
            param = {'id': request.POST['idresidence'], 'deb': request.POST['datedebut'], 'fin': request.POST['datefin']}
            cursor.execute(sql, params=param)
            rows = cursor.fetchall()
            if len(rows) > 0:
                return Response({"msg": "résidence indisponible", "resultat": False}, status=status.HTTP_201_CREATED)
            return Response({"msg": "résidence disponible", "resultat": True}, status=status.HTTP_201_CREATED)      