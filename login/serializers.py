from rest_framework import serializers

class LoginClientSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    
class MoyenneSerializer(serializers.Serializer):
    ville = serializers.CharField(max_length=200)
    quartier = serializers.CharField(max_length=200)
    prix_lte = serializers.IntegerField()
    prix_gte = serializers.IntegerField()
    
class MoyenneResiSerializer(serializers.Serializer):
    idresidence = serializers.CharField(max_length=200)
    idproprio = serializers.CharField(max_length=200)
    description = serializers.CharField()
    ville = serializers.CharField(max_length=200)
    quartier = serializers.CharField(max_length=200)
    prix = serializers.IntegerField()
    disponibilité = serializers.BooleanField()
    photocouverture = serializers.CharField(max_length=200)
    nbvote = serializers.IntegerField()
    moyenne = serializers.FloatField()
    
class Historiquemoyenresi(serializers.Serializer):
    idresidence = serializers.CharField(max_length=200)
    nbvisite3D = serializers.IntegerField()
    nbcommandeissu = serializers.IntegerField()
    nbvisitetotal = serializers.IntegerField()
    moyennetemps = serializers.FloatField()