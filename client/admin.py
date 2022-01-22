from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    
    list_display = ('nom', 'prenoms', 'phone', 'photo')
    
@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    
    list_display = ('idclient', 'idresidence', 'prixactuel', 'dateentree', 'dureeenjour', 'versementduclient', 'cleauclient', 'versementauproprio', 'datecommande', 'statucommande')
    list_filter = ('idclient', 'idresidence', 'dateentree', 'dureeenjour', 'datecommande', 'statucommande')
    
@admin.register(AjoutDeSejour)
class AjoutAdmin(admin.ModelAdmin):
    
    list_display = ('idcommande', 'dureeenjour', 'versementduclient', 'dateajout', 'statudemande')
    list_filter = ('dateajout', 'statudemande')
    
@admin.register(NoteResidence)
class NoteAdmin(admin.ModelAdmin):
    
    list_display = ('idclient', 'idresidence', 'note')
    list_filter = ('idclient', 'idresidence', 'note')
