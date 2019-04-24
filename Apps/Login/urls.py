from django.conf.urls import url
from django.contrib import admin
from Apps.Login.views import *
urlpatterns = [
	url(r'^$', Inicio, name='Inicio' ),
	url(r'^Entrar/$', Login, name='Login' ),
	url(r'^Salir/$', Logout, name='Logout' ),
  
]