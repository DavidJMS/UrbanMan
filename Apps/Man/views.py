from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from Apps.Productos.models import Categoria,Producto 
from Apps.Productos.forms import FormularioCategoria,FormularioProducto
import json 
from django.http import JsonResponse
#-------------------------------------ss-
#--------------------------------------
# Create your views here.

def Man(request):
	
	return render(request, 'Inicio/UrbanMan.html')

def Contactanos(request):
	
	return render(request, 'Inicio/Contactanos.html')

def Productos(request):
	
	return render(request, 'Inicio/Productos.html')

def Tienda(request):
	ListaProductos=Producto.objects.all()
	ListaCategoria= Categoria.objects.all()
	contexto={
			'ListaProductos':ListaProductos,
			'ListaCategoria':ListaCategoria,
			}
	return render(request, 'Productos/Ropa.html',contexto)
	if request.is_ajax():
		Productos = Producto.objects.filter(nombre__startswith= request.GET['nombre'] ).values('nombre', 'id')
		return HttpResponse( json.dumps( list(Productos)), content_type='application/json' ) 
	else:
	 	return HttpResponse("Solo Ajax")

def TiendaCategoria(request, id_Categoria1):
	Categoriaid = Categoria.objects.get(id= id_Categoria1)
	NombreCategoria = request.GET.get('Nombre_Categoria', None)
	Nombre= Categoriaid.Nombre
	ListaProductos=Producto.objects.filter(Categoria1 = Nombre )
	ListaCategoria= Categoria.objects.all()
	contexto={
			'ListaProductos':ListaProductos,
			'ListaCategoria':ListaCategoria,
			}
	return render(request, 'Productos/Ropa.html',contexto)

        
def Busqueda(request):
	Nombre1 = request.GET.get('nombre',None)
	ListaProductos = Producto.objects.filter(Nombre=Nombre1 )
	ListaCategoria= Categoria.objects.all()
	contexto= {
		'ListaProductos':ListaProductos,
		'ListaCategoria':ListaCategoria,
	}
	return render(request, 'Productos/Ropa.html',contexto) 