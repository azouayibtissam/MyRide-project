from django.shortcuts import render
from .models import Client
# Create your views here.
def home(request):
   return render(request, 'home.html')

def login(request):
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