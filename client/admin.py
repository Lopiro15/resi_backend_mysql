from django.contrib import admin

# Register your models here.
from client.models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    
    list_display = ('nom', 'prenoms', 'phone', 'photo', 'date')
    
@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    
    list_display = ('idclient', 'idresidence', 'prixactuel', 'datedebut', 'datefin', 'versementduclient', 'cleauclient', 'versementauproprio', 'datecommande', 'statucommande')
    list_filter = ('idclient', 'idresidence', 'datedebut', 'datefin', 'datecommande', 'statucommande')
    
@admin.register(AjoutDeSejour)
class AjoutAdmin(admin.ModelAdmin):
    
    list_display = ('idcommande', 'datefin', 'versementduclient', 'dateajout', 'statudemande')
    list_filter = ('dateajout', 'statudemande')
    
@admin.register(NoteResidence)
class NoteAdmin(admin.ModelAdmin):
    
    list_display = ('idclient', 'idresidence', 'note', 'date')
    list_filter = ('idclient', 'idresidence', 'note')
