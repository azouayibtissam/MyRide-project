from django.contrib import admin
from .models import Client, Vehicule, Voyage, Facture

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
   pass
   #list_display = ("nom_cl", "prenom_cl", "telephone")
admin.site.register(Client, ClientAdmin)


class VehiculeAdmin(admin.ModelAdmin):
   pass

admin.site.register(Vehicule, VehiculeAdmin)

class VoyageAdmin(admin.ModelAdmin):
   pass
admin.site.register(Voyage, VoyageAdmin)

class FactureAdmin(admin.ModelAdmin):
   pass
admin.site.register(Facture, FactureAdmin)