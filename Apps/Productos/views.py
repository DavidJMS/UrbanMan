from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from Apps.Productos.models import Categoria,Producto 
from Apps.Productos.forms import FormularioCategoria,FormularioProducto

def NuevaCategoria(request):
	Form = FormularioCategoria()
	if request.method == 'POST':
		Form  = FormularioCategoria(request.POST, request.FILES  or None)
		if Form.is_valid():
			Form.save()
			return redirect('Producto:ListadeCategorias')
			
		else:
			print('Error datos invalidos')
	contexto = {
		'Form':Form
	}
	return render(request, 'Productos/NuevaCategoria.html', contexto)

def NuevoProducto(request):
	Form = FormularioProducto()
	if request.method == 'POST':
		Form  = FormularioProducto(request.POST, request.FILES  or None)
		if Form.is_valid():
			Form.save()
			return redirect('Producto:ListadeProductos')
			
		else:
			print('Error datos invalidos')
	contexto = {
		'Form':Form
	}
	return render(request, 'Productos/NuevoProducto.html', contexto)

def ListadeCategorias(request):
	ListaCategorias= Categoria.objects.all()
	contexto={
			'ListaCategorias':ListaCategorias,
			}
	return render(request,'Productos/ListadeCategorias.html',contexto)

def ListadeProductos(request):
	ListaProductos=Producto.objects.all()
	contexto={
			'ListaProductos':ListaProductos,
			}
	return render(request,'Productos/ListadeProductos.html',contexto)

def EliminarCategoria(request):
	status = None
	id_Categoria = request.GET.get('id_Categoria', None)
	query = Categoria.objects.get( id = id_Categoria)
	query.delete()
	status = 200
	return HttpResponse(status) 

def EliminarProducto(request):
	status = None
	id_Producto = request.GET.get('id_Producto', None)
	query = Producto.objects.get( id = id_Producto)
	query.delete()
	status = 200
	return HttpResponse(status) 
	

def EditarCategoria(request , id_Categoria1):
	NuevaCategoria = Categoria.objects.get(id = id_Categoria1)
	if request.method == 'GET':
		Form = FormularioCategoria(instance = NuevaCategoria)
	else:
		Form = Categoria(request.POST,  request.FILES, instance = NuevaCategoria)
		if Form.is_valid():
			Form.save()
			return redirect('Producto:ListadeCategorias' ,)
	contexto = {
	 	'NuevaCategoria':NuevaCategoria,
	 	'Form':Form
	}
	return render(request, 'Productos/NuevaCategoria.html', contexto)

def EditarProducto(request , id_Producto1):
	Producto1 = Producto.objects.get(id = id_Producto1)
	if request.method == 'GET':
		Form = FormularioProducto(instance = Producto1)
	else:
		Form = FormularioProducto(request.POST,  request.FILES, instance = Producto1)
		if Form.is_valid():
			Form.save()
			return redirect('Producto:ListadeProductos' ,)
	contexto = {
	 	'Producto1':Producto1,
	 	'Form':Form
	}
	return render(request, 'Productos/NuevoProducto.html', contexto)

def DetalleProducto(request, id_Producto):
	Producto1 = Producto.objects.get(id= id_Producto)
	contexto ={
			'Producto1' : Producto1,
	}
	return render(request , 'Productos/DetalleProducto.html', contexto)

def DetalleCategoria(request, id_Categoria1):
	Categoria1 = Categoria.objects.get(id= id_Categoria1)
	contexto ={
			'Categoria1' : Categoria1,
	}
	return render(request , 'Productos/DetalleCategoria.html', contexto)