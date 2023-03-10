from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Client
from . import forms
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib import messages
# Create your views here.
def home(request):
   return render(request, 'home.html', {'test': "ibtissam"})

def login(request):
	if(request.method == "POST"):
		mail = request.POST["mail"]
		password = request.POST["password"]
		existing_client=None
		try:
			existing_client=Client.objects.get(mail=mail, password=password)
		except:
			print("mail or password incorrect")

		if existing_client:
			request.session['current_user'] = {'prenom_cl': existing_client.prenom_cl, 'nom_cl': existing_client.nom_cl}
			return render(request, 'voyage.html')
		else:
			return render(request, 'login.html', {'error_login': "mail or password incorrect !"})
	return render(request, 'login.html')
		

	
def signup(request):
	if(request.method == "POST"):
		nom = request.POST["nom"]
		prenom = request.POST["prenom"]
		mail = request.POST["email"]
		password = request.POST["password"]
		telephone=request.POST["telephone"]
		adresse= request.POST["adresse"]
		c = Client(nom_cl=nom, prenom_cl=prenom, mail= mail, password=password, telephone= telephone, adresse=adresse)
		existing_client=None
		try:
			existing_client = Client.objects.get(mail=mail)
		except:
			print("client not found")
		if(existing_client):
			print(existing_client.mail, "@ already taken")
			return render(request, 'signup.html', {'error_mail': "Email address already in use !"})
		if(len(password)<6):
			return render(request, 'signup.html', {'error_pass': "Password must be longer than 6 characters !"})
		c.save()
		messages.success(request, 'votre compte a été créé avec succès !')
		# return redirect('login')
	return render(request, 'signup.html')

def mdp(request):
   return render(request, 'mdp.html')

def up_succes(request):
   return render(request, 'up_succes.html')

def voyage(request):
	# , client=None
	if(not request.session["current_user"]):
		return render(request, 'login.html', {'error_login': "You must be logged in to access voyage page!"})
	print(request.session["current_user"], "session opened!!!!!!!!")
	return render(request, 'voyage.html' )

def detail(request):
   return render(request, 'detail.html')
   
#contactus
def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'contactsuccess.html')
    return render(request, 'contactus.html', {'form':sub})

def scan(request):
   return render(request, 'scan.html')

def disconnect(request):
   del request.session["current_user"]
   return render(request, 'login.html')

def vehicules(request):
   return render(request, 'vehicules.html')

def facture(request):
   return render(request, 'facture.html')