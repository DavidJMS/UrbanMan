from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
#-------------------------------------ss-
#--------------------------------------
# Create your views here.

def Man(request):
	
	return render(request, 'Inicio/UrbanMan.html')

def Contactanos(request):
	
	return render(request, 'Inicio/Contactanos.html')

def Productos(request):
	
	return render(request, 'Inicio/Productos.html')
