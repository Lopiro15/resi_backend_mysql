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
        'Page Administrateur' : '/admin/',
        'Gestion de l\'API client' : '/client/',
        'Connection du client' : '/login/client/',
        'Connection du proprietaire' : '/login/proprio/',
        'Modifier le password d\'un client' : '/changepassword/client/',
        'Modifier le password d\'un proprietaire' : '/changepassword/proprio/',
        'Gestion de l\'API proprietaire' : '/proprio/',
        'Liste des residences avec leurs évaluations moyennes' : '/moyenneresi/',
        'Historique des visites en moyenne des résidences' : '/historiquemoyenresi/',
        'Vérifier la disponibilité d\'une residence' : '/disponibiliteresi/',
        'Confirmer une commande': '/confirmation-commande/',
        'La liste des commande et des residences en attente de confirmation': 'commande_en_attente/',
        'Documentation' : '/swagger/',
    }
    return Response(context)



@swagger_auto_schema(method='get', responses={201: MoyenneResiSerializer})
@swagger_auto_schema(method='post', request_body=MoyenneSerializer, responses={201: MoyenneResiSerializer})
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def resi_note(request, format=None):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            sql = "SELECT proprio_residence.*, COUNT(client_noteresidence.note) as nbvote, AVG(client_noteresidence.note) as moyenne FROM proprio_residence, client_noteresidence WHERE proprio_residence.id = client_noteresidence.idresidence_id GROUP BY client_noteresidence.idresidence_id ORDER BY moyenne;"
            cursor.execute(sql)
            rows = cursor.fetchall()
            json_data = []
            for obj in rows:
                json_data.append({"idresidence" : obj[0], "idproprio" : obj[1], "description" : obj[2], "ville" : obj[3], "quartier" : obj[4], "prix" : obj[5], "disponibilité" : obj[6], "photocouverture" : obj[7], "nbvote" : obj[8], "moyenne" : obj[9]})
        return Response(json_data, status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        with connection.cursor() as cursor:
            sql = "SELECT proprio_residence.*, COUNT(client_noteresidence.note) as nbvote, AVG(client_noteresidence.note) as moyenne FROM proprio_residence, client_noteresidence WHERE proprio_residence.id = client_noteresidence.idresidence_id AND proprio_residence.disponibilité = 1 AND proprio_residence.ville LIKE %(v)s AND proprio_residence.quartier LIKE %(q)s AND proprio_residence.prix <= %(p_lte)s AND proprio_residence.prix >= %(p_gte)s GROUP BY client_noteresidence.idresidence_id ORDER BY moyenne;"
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
        sql= "SELECT proprio_historiqueresi.idresidence_id, annonce3D.nbvisite3D, annoncecommande.nbcommande, COUNT(tempssurannonce) as nbvisite, AVG(tempssurannonce) as moyenne FROM proprio_historiqueresi, annonce3D, annoncecommande WHERE proprio_historiqueresi.idresidence_id = annonce3D.idresidence_id AND proprio_historiqueresi.idresidence_id = annoncecommande.idresidence_id GROUP BY proprio_historiqueresi.idresidence_id ORDER BY moyenne"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            json_data.append({"idresidence" : row[0], "nbvisite3D" : row[1], "nbcommandeissu" : row[2], "nbvisitetotal" : row[3], "moyennetemps" : row[4]})
    return Response(json_data, status=status.HTTP_201_CREATED)
     

@swagger_auto_schema(method='get', request_body=DisporesiSerializer, responses={201: DisporesiresultSerializer})   
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def disponibilite_une_resi(Format=None, **kwargs):
    with connection.cursor() as cursor:
        sql = "SELECT proprio_residence.*, client_commande.prixactuel, client_commande.datedebut, client_commande.datefin, client_commande.datecommande FROM client_commande, proprio_residence WHERE client_commande.statucommande = 'VALIDE' AND proprio_residence.id = client_commande.idresidence_id AND proprio_residence.id = %(idresi)s AND (client_commande.datedebut > %(fin)s OR client_commande.datefin < %(deb)s)"
        param = {'idresi': kwargs['idresidence'], 'deb': kwargs['datedebut'], 'fin': kwargs['datefin']}
        cursor.execute(sql, params=param)
        rows = cursor.fetchall()
        json_data = []
        for row in rows:
            json_data.append({"id": row[0], "nbpiece": row[1], "description": row[2], "ville": row[3], "quartier": row[4], "prix_journalier": row[5], "disponibilité": row[6], "photo_couverture": row[7], "date": row[8], "idproprio": row[9], "nbcommande": row[10]})
        return Response(json_data, status=status.HTTP_201_CREATED)

@swagger_auto_schema(method='get', request_body=DisporesiSerializer, responses={201: DisporesiresultSerializer})   
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def disponibilite_resis(Format=None, **kwargs):
    with connection.cursor() as cursor:
        sql = "SELECT proprio_residence.*, client_commande.prixactuel, client_commande.datedebut, client_commande.datefin, client_commande.datecommande FROM client_commande, proprio_residence WHERE client_commande.statucommande = 'VALIDE' AND proprio_residence.id = client_commande.idresidence_id AND (client_commande.datedebut > %(fin)s OR client_commande.datefin < %(deb)s)"
        param = {'deb': kwargs['datedebut'], 'fin': kwargs['datefin'], 'idproprio': kwargs['idproprio']}
        cursor.execute(sql, params=param)
        rows = cursor.fetchall()
        json_data = []
        for row in rows:
            json_data.append({"id": row[0], "nbpiece": row[1], "description": row[2], "ville": row[3], "quartier": row[4], "prix_journalier": row[5], "disponibilité": row[6], "photo_couverture": row[7], "date": row[8], "idproprio": row[9], "nbcommande": row[10]})
        return Response(json_data, status=status.HTTP_201_CREATED)

@swagger_auto_schema(method='get', request_body=DisporesiSerializer, responses={201: DisporesiresultSerializer})   
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def historique_resis(Format=None, **kwargs):
    with connection.cursor() as cursor:
        sql = "SELECT proprio_residence.*, client_commande.prixactuel, client_commande.datedebut, client_commande.datefin, client_commande.datecommande FROM client_commande, proprio_residence WHERE client_commande.statucommande = 'VALIDE' AND proprio_residence.id = client_commande.idresidence_id AND (client_commande.datedebut <= %(fin)s AND client_commande.datefin >= %(deb)s)"
        param = {'deb': kwargs['datedebut'], 'fin': kwargs['datefin'], 'idproprio': kwargs['idproprio']}
        cursor.execute(sql, params=param)
        rows = cursor.fetchall()
        json_data = []
        for row in rows:
            json_data.append({"id": row[0], "nbpiece": row[1], "description": row[2], "ville": row[3], "quartier": row[4], "prix_journalier": row[5], "disponibilité": row[6], "photo_couverture": row[7], "date": row[8], "idproprio": row[9], "nbcommande": row[10]})
        return Response(json_data, status=status.HTTP_201_CREATED)

@swagger_auto_schema(method='get', request_body=ConfirmCommandeSerializer, responses={201: ConfirmCommanderesultSerializer})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def confirmation_de_la_commande(request, Format=None, **kwargs):
    with connection.cursor() as cursor:
        req = "SELECT * FROM client_commande WHERE id = %(id)s"
        param = {'id': kwargs['idcommande']}
        cursor.execute(req, params=param)
        rows = cursor.fetchall()
        for row in rows:
            debut = row[2]
            fin = row[3]
            resi = row[10]
        if len(rows) > 0:
            sql = "UPDATE client_commande SET statucommande = 'VALIDE' WHERE id = %(id)s"
            param = {'id': kwargs['idcommande']}
            cursor.execute(sql, params=param)
            sql2 = "UPDATE client_commande SET statucommande = 'ANNULE' WHERE statucommande = 'ATTENTE' AND idresidence_id = %(idresidence)s AND datedebut <= %(fin)s AND datefin >= %(deb)s"
            params = {'idresidence': resi, 'deb': debut, 'fin': fin}
            cursor.execute(sql2, params=params)
            return Response({"msg": "commande confirmé", "resultat": True}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "commande inexistante", "resultat": False}, status=status.HTTP_200_OK)

@swagger_auto_schema(method='get', request_body=ConfirmCommandeSerializer, responses={201: ConfirmCommanderesultSerializer})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def annulation_de_la_commande(request, Format=None, **kwargs):
    with connection.cursor() as cursor:
        req = "SELECT * FROM client_commande WHERE id = %(id)s"
        param = {'id': kwargs['idcommande']}
        cursor.execute(req, params=param)
        rows = cursor.fetchall()
        if len(rows) > 0:
            sql = "UPDATE client_commande SET statucommande = 'ANNULE' WHERE id = %(id)s"
            param = {'id': kwargs['idcommande']}
            cursor.execute(sql, params=param)
            return Response({"msg": "commande confirmé", "resultat": True}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "commande inexistante", "resultat": False}, status=status.HTTP_200_OK)  

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def commande_en_attente_de_confirmation(request, Format=None,  **kwargs):
    with connection.cursor() as cursor:
            sql = "SELECT proprio_residence.*, client_commande.prixactuel, client_commande.datedebut, client_commande.datefin, client_commande.datecommande, client_client.* FROM proprio_residence, client_commande, client_client WHERE client_commande.statucommande = 'ATTENTE' AND proprio_residence.id = client_commande.idresidence_id AND client_commande.idclient_id = client_client.id AND proprio_residence.idproprio_id = %(id)s ORDER BY client_commande.datecommande DESC;"
            param = {'id': kwargs['pk']}
            cursor.execute(sql=sql, params=param)
            rows = cursor.fetchall()
            json_data = []
            for row in rows:
                json_data.append({"id": row[0], "nbpiece": row[1], "description": row[2], "ville": row[3], "quartier": row[4], "prix_journalier": row[5], "disponibilité": row[6], "photo_couverture": row[7], "date": row[8], "idproprio": row[9], "prixactuel": row[10], "date_debut": row[11], "date_fin": row[12], "datecommande": row[13], "idclient": row[13], "nom_client": row[14], "prenoms_client": row[15], "phone": row[16]})
            return Response(json_data, status=status.HTTP_201_CREATED)

@permission_classes([IsAuthenticated])        
@api_view(['GET'])
def resi_commande_en_attente(request, Format=None,  **kwargs):
    with connection.cursor() as cursor:
            sql = "SELECT proprio_residence.*, COUNT(client_commande.prixactuel) as nbcommande FROM proprio_residence, client_commande WHERE client_commande.statucommande = 'ATTENTE' AND proprio_residence.id = client_commande.idresidence_id AND proprio_residence.idproprio_id = %(id)s GROUP BY proprio_residence.id ORDER BY client_commande.datecommande DESC;"
            param = {'id': kwargs['pk']}
            cursor.execute(sql=sql, params=param)
            rows = cursor.fetchall()
            json_data = []
            for row in rows:
                json_data.append({"id": row[0], "nbpiece": row[1], "description": row[2], "ville": row[3], "quartier": row[4], "prix_journalier": row[5], "disponibilité": row[6], "photo_couverture": row[7], "date": row[8], "idproprio": row[9], "nbcommande": row[10]})
            return Response(json_data, status=status.HTTP_201_CREATED)
      