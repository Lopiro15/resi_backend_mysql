from rest_framework import serializers
from client.models import AjoutDeSejour, Client, Commande, NoteResidence

# Client Serializer
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'
        
class AjoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AjoutDeSejour
        fields = '__all__'
        
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteResidence
        fields = '__all__'