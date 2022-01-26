from django.db import models
from client.models import NoteResidence


# Create your models here.
class Proprietaire(models.Model):
    nom = models.CharField(null=False, max_length=25)
    prenoms = models.CharField(null=False, max_length=75)
    phone = models.CharField(null=False, max_length=10)
    photo = models.ImageField(upload_to ='proprio/image/', null=True)
    username = models.CharField(null=False, max_length=255, unique=True)
    password = models.CharField(null=False, max_length=255)
    
class Residence(models.Model):
    idproprio = models.CharField(null=False, max_length=255)
    descriptifresidence = models.TextField(null=False)
    ville = models.CharField(null=False, max_length=100)
    quartier = models.CharField(null=False, max_length=100)
    prix = models.IntegerField(null=False)
    disponibilité = models.BooleanField(default=True)
    photocouverture = models.ImageField(upload_to ='proprio/image/resi/', null=True)
    
class Imageresi(models.Model):
    idresidence = models.CharField(null=False, max_length=255)
    image = models.ImageField(upload_to ='proprio/image/resi/')
    
class Historiqueresi(models.Model):
    date = models.DateField(auto_now_add=True)
    idresidence = models.CharField(null=False, max_length=255)
    idclient = models.CharField(null=False, max_length=255)
    duredesejour = models.IntegerField(null=False)
    visite3D = models.BooleanField(default=False)
    residencecommandé = models.BooleanField(default=True)
