from django.db import models




# Create your models here.
class Client(models.Model):
    nom = models.CharField(null=False, max_length=25)
    prenoms = models.CharField(null=False, max_length=75)
    phone = models.CharField(null=False, max_length=10)
    photo = models.ImageField(upload_to ='client/image/', null=True)
    username = models.CharField(null=False, max_length=255, unique=True)
    password = models.CharField(null=False, max_length=255)
    
class Commande(models.Model):
    
    CHOICES = (
        ('ATTENTE', 'En attente'),
        ('VALIDE', 'Validé'),
        ('ANNULE', 'Annulé'),
    )
    
    idclient = models.CharField(null=False, max_length=255)
    idresidence = models.CharField(null=False, max_length=255)
    prixactuel = models.IntegerField(null=False)
    dateentree = models.DateField(auto_now=False, auto_now_add=False)
    dureeenjour = models.IntegerField(null=False)
    versementduclient = models.BooleanField(default=False)
    cleauclient = models.BooleanField(default=False)
    versementauproprio = models.BooleanField(default=False)
    datecommande = models.DateField(auto_now_add=True)
    statucommande = models.CharField(null=False, max_length=100, choices = CHOICES)
    
class AjoutDeSejour(models.Model):
    
    CHOICES = (
        ('ATTENTE', 'En attente'),
        ('VALIDE', 'Validé'),
        ('ANNULE', 'Annulé'),
    )
    
    idcommande = models.CharField(null=False, max_length=255)
    dureeenjour = models.IntegerField(null=False)
    versementduclient = models.BooleanField(default=False)
    dateajout = models.DateField(auto_now_add=True)
    statudemande = models.CharField(null=False, max_length=100, choices = CHOICES)

class NoteResidence(models.Model):
    
    CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (3, '4'),
        (5, '5'),
    )
    
    idclient = models.CharField(null=False, max_length=255)
    idresidence = models.CharField(null=False, max_length=255)
    note = models.IntegerField(null=False, choices = CHOICES)
