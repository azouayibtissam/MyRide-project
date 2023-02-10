from django.db import models

# Create your models here.

class Client(models.Model):
    nom_cl = models.CharField(max_length=30)
    prenom_cl = models.CharField(max_length=30)
    mail=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    telephone = models.IntegerField()
    adresse=models.CharField(max_length=30)    
    
class Vehicule(models.Model):
    designation = models.CharField(max_length=30)
    model= models.CharField(max_length=30)
    photo=models.ImageField(upload_to='vehicules', default=None)
    date_achat= models.DateField()
    prix_achat= models.DecimalField(max_digits=5,decimal_places=1)
    tarif_heure= models.IntegerField()
    disponible=models.BooleanField()


class Voyage(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    #vehicule= models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    heure_debut = models.DateField()
    heure_fin= models.DateField()

class Facture(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    montant= models.IntegerField()

class Comment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_comment = models.DateField()
    msg= models.CharField(max_length=200)