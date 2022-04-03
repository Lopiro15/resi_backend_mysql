from django.db import models





# Create your models here.
class Client(models.Model):
    nom = models.CharField(null=False, max_length=25)
    prenoms = models.CharField(null=False, max_length=75)
    phone = models.CharField(null=False, max_length=10)
    photo = models.ImageField(upload_to ='client/image/', null=True)
    username = models.CharField(null=False, max_length=255, unique=True)
    user_id = models.ForeignKey('User.CustomUser', null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
class Commande(models.Model):
    
    CHOICES = (
        ('ATTENTE', 'En Attente'),
        ('VALIDE', 'Validé'),
        ('ANNULE', 'Annulé'),
    )
    
    idclient = models.ForeignKey(Client, null=False, on_delete=models.CASCADE)
    idresidence = models.ForeignKey('proprio.Residence', null=False, on_delete=models.CASCADE)
    prixactuel = models.IntegerField(null=False)
    datedebut = models.DateField(auto_now=False, auto_now_add=False)
    datefin = models.DateField(auto_now=False, auto_now_add=False)
    versementduclient = models.BooleanField(default=False)
    cleauclient = models.BooleanField(default=False)
    versementauproprio = models.BooleanField(default=False)
    datecommande = models.DateTimeField(auto_now_add=True)
    statucommande = models.CharField(null=False, max_length=100, choices = CHOICES)
    
    class Meta:
        ordering = ('-datecommande',)
    
class AjoutDeSejour(models.Model):
    
    CHOICES = (
        ('ATTENTE', 'En Attente'),
        ('VALIDE', 'Validé'),
        ('ANNULE', 'Annulé'),
    )
    
    idcommande = models.ForeignKey(Commande, null=False, on_delete=models.CASCADE)
    datefin = models.DateField(null=True, auto_now=False, auto_now_add=False)
    versementduclient = models.BooleanField(default=False)
    dateajout = models.DateTimeField(auto_now_add=True)
    statudemande = models.CharField(null=False, max_length=100, choices = CHOICES)

class NoteResidence(models.Model):
    
    CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (3, '4'),
        (5, '5'),
    )
    
    idclient = models.ForeignKey(Client, null=False, on_delete=models.CASCADE)
    idresidence = models.ForeignKey('proprio.Residence', null=False, on_delete=models.CASCADE)
    note = models.IntegerField(null=False, choices = CHOICES)
    date = models.DateTimeField(auto_now_add=True)
