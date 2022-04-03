from django.contrib import admin

# Register your models here.
from proprio.models import *
from client.models import *

class ResidenceInline(admin.TabularInline):
    model = Residence
    
class CommandeInline(admin.TabularInline):
    model = Commande

class NoteInline(admin.TabularInline):
    model = NoteResidence
    
class PieceInline(admin.TabularInline):
    model = Piecesresi
    
class ImagePieceInline(admin.TabularInline):
    model = Imagepieceresi
    
class HistoriqueresiInline(admin.TabularInline):
    model = Historiqueresi

@admin.register(Proprietaire)
class ProprioAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'nom', 'prenoms', 'phone', 'photo', 'piece_identite', 'isactivate', 'date')
    inlines = (ResidenceInline,)
    
@admin.register(Residence)
class ResiAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'idproprio', 'descriptifresidence', 'ville', 'quartier', 'prixjournalier', 'disponibilite', 'photocouverture', 'date')
    list_filter = ('idproprio', 'ville', 'quartier', 'prixjournalier', 'disponibilite')
    inlines = (PieceInline, CommandeInline, NoteInline, HistoriqueresiInline)
    
@admin.register(Piecesresi)
class PieceAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'idresidence', 'nompiece')
    list_filter = ('idresidence', 'nompiece')
    inlines = (ImagePieceInline,)

@admin.register(Imagepieceresi)
class ImagePieceAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'idpiece', 'image')
    

@admin.register(Historiqueresi)
class HistoriqueAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'date', 'idresidence', 'idclient', 'tempssurannonce', 'visite3D', 'residencecommandé')
    list_filter = ('idresidence', 'idclient', 'visite3D')
