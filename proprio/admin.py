from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Proprietaire)
class ProprioAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'nom', 'prenoms', 'phone', 'photo')
    
@admin.register(Residence)
class ResiAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'idproprio', 'descriptifresidence', 'ville', 'quartier', 'prix', 'disponibilité', 'photocouverture')
    list_filter = ('idproprio', 'ville', 'quartier', 'prix', 'disponibilité')
    
@admin.register(Historiqueresi)
class ProprioAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'date', 'idresidence', 'idclient', 'duredesejour', 'visite3D', 'residencecommandé')
    list_filter = ('idresidence', 'idclient', 'visite3D')
