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
    photo=models.ImageField(upload_to='static/vehicules', default=None)
    date_achat= models.DateField()
    prix_achat= models.DecimalField(max_digits=5,decimal_places=1)
    tarif_heure= models.IntegerField()
    disponible=models.BooleanField()


class Voyage(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vehicule= models.ForeignKey(Vehicule, on_delete=models.CASCADE, default=None)
    heure_debut = models.CharField(max_length=30)
    heure_fin= models.CharField(max_length=30)
    montant= models.DecimalField(max_digits=5,decimal_places=2, default=0) 


class Comment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_comment = models.CharField(max_length=30)
    msg= models.CharField(max_length=200)