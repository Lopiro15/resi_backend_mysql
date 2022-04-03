from django.db import models


# Create your models here.
class Proprietaire(models.Model):
    nom = models.CharField(null=False, max_length=25)
    prenoms = models.CharField(null=False, max_length=75)
    phone = models.CharField(null=False, max_length=10)
    photo = models.ImageField(upload_to ='image/profile/', null=True)
    username = models.CharField(null=False, max_length=255, unique=True)
    user_id = user_id = models.ForeignKey('User.CustomUser', null=True, on_delete=models.CASCADE)
    piece_identite = models.ImageField(upload_to ='image/profile/', null=True)
    isactivate = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
class Residence(models.Model):
    idproprio = models.ForeignKey(Proprietaire, on_delete=models.CASCADE, null=False)
    nbpieces = models.IntegerField(null=False)
    descriptifresidence = models.TextField(null=False)
    ville = models.CharField(null=False, max_length=100)
    quartier = models.CharField(null=False, max_length=100)
    prixjournalier = models.IntegerField(null=False)
    disponibilite = models.BooleanField(default=True)
    photocouverture = models.ImageField(upload_to ='image/resi/', null=True)
    date = models.DateTimeField(auto_now_add=True)
    

class Piecesresi(models.Model):
    idresidence = models.ForeignKey(Residence, null=False, on_delete=models.CASCADE)
    nompiece = models.CharField(null=False, max_length=100)

class Imagepieceresi(models.Model):
    idpiece = models.ForeignKey(Piecesresi, null=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='image/resi/')
    
class Historiqueresi(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    idresidence = models.ForeignKey(Residence, null=False, on_delete=models.CASCADE)
    idclient = models.ForeignKey('client.Client', on_delete=models.CASCADE, null=False)
    tempssurannonce = models.IntegerField(null=False)
    visite3D = models.BooleanField(default=False)
    residencecommandé = models.BooleanField(default=True)
