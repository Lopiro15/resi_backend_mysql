from django.contrib import admin

# Register your models here.
from client.models import *
from proprio.models import Historiqueresi


class CommandeInline(admin.TabularInline):
    model = Commande
    
class HistoriqueresiInline(admin.TabularInline):
    model = Historiqueresi

class AjoutInline(admin.TabularInline):
    model = AjoutDeSejour

class NoteInline(admin.TabularInline):
    model = NoteResidence

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    
    list_display = ('nom', 'prenoms', 'phone', 'photo', 'date')
    inlines = (CommandeInline, NoteInline, HistoriqueresiInline)
    
@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    
    list_display = ('idclient', 'idresidence', 'prixactuel', 'datedebut', 'datefin', 'versementduclient', 'cleauclient', 'versementauproprio', 'datecommande', 'statucommande')
    list_filter = ('idclient', 'idresidence', 'datedebut', 'datefin', 'datecommande', 'statucommande')
    inlines = (AjoutInline,)
    
@admin.register(AjoutDeSejour)
class AjoutAdmin(admin.ModelAdmin):
    
    list_display = ('idcommande', 'datefin', 'versementduclient', 'dateajout', 'statudemande')
    list_filter = ('dateajout', 'statudemande')
    
@admin.register(NoteResidence)
class NoteAdmin(admin.ModelAdmin):
    
    list_display = ('idclient', 'idresidence', 'note', 'date')
    list_filter = ('idclient', 'idresidence', 'note')
