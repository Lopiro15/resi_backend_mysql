from django.contrib import admin

# Register your models here.
from proprio.models import *

@admin.register(Proprietaire)
class ProprioAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'nom', 'prenoms', 'phone', 'photo', 'piece_identite', 'isactivate', 'date')
    
@admin.register(Residence)
class ResiAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'idproprio', 'descriptifresidence', 'ville', 'quartier', 'prixjournalier', 'disponibilité', 'photocouverture', 'date')
    list_filter = ('idproprio', 'ville', 'quartier', 'prixjournalier', 'disponibilité')
    
@admin.register(Piecesresi)
class PieceAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'idresidence', 'nompiece')
    list_filter = ('idresidence', 'nompiece')

@admin.register(Imagepieceresi)
class ImagePieceAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'idpiece', 'image')
    

@admin.register(Historiqueresi)
class HistoriqueAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'date', 'idresidence', 'idclient', 'tempssurannonce', 'visite3D', 'residencecommandé')
    list_filter = ('idresidence', 'idclient', 'visite3D')
