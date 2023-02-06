from django.contrib import admin
from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
   pass
   #list_display = ("nom_cl", "prenom_cl", "telephone")
admin.site.register(Client, ClientAdmin)