from rest_framework import serializers
from proprio.models import Historiqueresi, Imageresi, Proprietaire, Residence

# Client Serializer
class ProprietaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietaire
        fields = '__all__'
        

class ImageResiserializer(serializers.ModelSerializer):
    class Meta:
        model = Imageresi
        fields = '__all__'
        
class Resiserializer(serializers.ModelSerializer):

    class Meta:
        model = Residence
        fields = '__all__'
        
class HistoriqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historiqueresi
        fields = '__all__'
    