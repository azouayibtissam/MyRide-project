from django.contrib import admin
from .models import Client, Vehicule

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
   pass
   #list_display = ("nom_cl", "prenom_cl", "telephone")
admin.site.register(Client, ClientAdmin)


class VehiculeAdmin(admin.ModelAdmin):
   pass
   #list_display = ("nom_cl", "prenom_cl", "telephone")
admin.site.register(Vehicule, VehiculeAdmin)