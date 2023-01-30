from django.db import models

# Create your models here.

class Client(models.Model):
    nom_cl = models.CharField(max_length=30)
    prenom_cl = models.CharField(max_length=30)
    mail=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    telephone = models.IntegerField()
    adresse=models.CharField(max_length=30)
    



# class Voyage(models.Model):
#     id_client = models.BigAutoField(primary_key=True)
#     heure_debut = models.DateField(max_length=30)
#     heure_fin= models.CharField(max_length=30)
    
