from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from .models import Client
from . import forms
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):
   return render(request, 'home.html')

def login(request):
	if(request.method == "POST"):
		mail = request.POST["email"]
		password = request.POST["password"]
		checking_user=Client(mail=mail)
		checking_password=Client(password=password)
		if (mail==checking_user) and (password==checking_password):
			return render(request, 'voyage.html')
		
		try:
			checking_user= Client.objects.get(mail=mail, password=password)
			
		except:
			print("mail or password incorrect")
	
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
			error={}
			error["msg"]="Mail aleady taken"
			if error:
				print(error["msg"])
			return render(request, 'signup.html', error)
		else:
			c.save()
			

		#print("test", existing_client)

	return render(request, 'signup.html')

def mdp(request):
   return render(request, 'mdp.html')

def voyage(request):
   return render(request, 'voyage.html')


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