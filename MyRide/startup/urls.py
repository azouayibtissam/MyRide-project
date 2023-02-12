from django import views
from django.urls import path, include
from .views import *
urlpatterns = [
    path('',home, name="home"),
    path('login',login, name="login"),
    path('signup',signup, name="signup"),
    path('mdp',mdp, name="mdp"),
    path('voyage', voyage, name="voyage"),
    path('contactus', contactus_view, name="contactus"),
    path('detail', detail, name="detail"),
    path('scan', scan, name="scan"),
    path('up_succes', up_succes, name="up_succes"),
    path('disconnect', disconnect, name="disconnect"),

    
]
