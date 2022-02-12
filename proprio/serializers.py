from rest_framework import serializers
from proprio.models import *

# Client Serializer
class ProprietaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietaire
        fields = '__all__'
        

class ImagePieceResiserializer(serializers.ModelSerializer):
    class Meta:
        model = Imagepieceresi
        fields = '__all__'

class PiecesResiserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Piecesresi
        fields = '__all__'
        
class Resiserializer(serializers.ModelSerializer):

    class Meta:
        model = Residence
        fields = '__all__'
        
class HistoriqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historiqueresi
        fields = '__all__'
    