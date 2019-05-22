from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from Apps.Productos.models import Categoria,Producto 
from Apps.Productos.forms import FormularioCategoria,FormularioProducto
from Apps.Carrito.models import CompraTemporal,CompraRelalizada
from Apps.Carrito.models import Metodo
from Apps.Carrito.forms import FormularioMetodo
from django.contrib.auth.decorators import login_required
@login_required(login_url = 'Login:Login' )
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

@login_required(login_url = 'Login:Login' )
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

@login_required(login_url = 'Login:Login' )
def ListadeCategorias(request):
	ListaCategorias= Categoria.objects.all()
	contexto={
			'ListaCategorias':ListaCategorias,
			}
	return render(request,'Productos/ListadeCategorias.html',contexto)

@login_required(login_url = 'Login:Login' )
def ListadeProductos(request):
	ListaProductos=Producto.objects.all()
	contexto={
			'ListaProductos':ListaProductos,
			}
	return render(request,'Productos/ListadeProductos.html',contexto)

@login_required(login_url = 'Login:Login' )
def EliminarCategoria(request):
	status = None
	id_Categoria = request.GET.get('id_Categoria', None)
	query = Categoria.objects.get( id = id_Categoria)
	query.delete()
	status = 200
	return HttpResponse(status) 

@login_required(login_url = 'Login:Login' )
def EliminarProducto(request):
	status = None
	id_Producto = request.GET.get('id_Producto', None)
	query = Producto.objects.get( id = id_Producto)
	query.delete()
	status = 200
	return HttpResponse(status) 
	
@login_required(login_url = 'Login:Login' )
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

@login_required(login_url = 'Login:Login' )
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
@login_required(login_url = 'Login:Login' )
def DetalleProducto(request, id_Producto):
	Producto1 = Producto.objects.get(id= id_Producto)
	contexto ={
			'Producto1' : Producto1,
	}
	return render(request , 'Productos/DetalleProducto.html', contexto)

@login_required(login_url = 'Login:Login' )
def DetalleCategoria(request, id_Categoria1):
	Categoria1 = Categoria.objects.get(id= id_Categoria1)
	contexto ={
			'Categoria1' : Categoria1,
	}
	return render(request , 'Productos/DetalleCategoria.html', contexto)

@login_required(login_url = 'Login:Login' )
def CarritoTemporal(request):
	response = None
	Usuario = request.GET.get('id_Producto', None)
	Nombre = request.GET.get('Nombre_Producto', None)
	Descripcion = request.GET.get('Precio_Producto', None)
	Precio = request.GET.get('descripcion_Producto', None)
	Nuevacompra = CompraTemporal()
	Nuevacompra2= CompraRelalizada()
	Nuevacompra.Usuario = request.user.id
	Nuevacompra.Nombre = Nombre
	Nuevacompra.Descripcion = Descripcion
	Nuevacompra.Precio = Precio
	Nuevacompra2.Usuario = request.user.id
	Nuevacompra2.Nombre = Nombre
	Nuevacompra2.Descripcion = Descripcion
	Nuevacompra2.Precio = Precio
	Nuevacompra2.FechaPago='1000-01-01'
	Nuevacompra.save()
	NuevaCompra= CompraTemporal.objects.all().last()
	Nuevacompra2.id2 = Nuevacompra.id	
	Nuevacompra2.save()
	response = 200
	return HttpResponse(response)

@login_required(login_url = 'Login:Login' )
def MetodoVista(request):
	Form = FormularioMetodo()
	if request.method == 'POST':
		Form  = FormularioMetodo(request.POST, request.FILES  or None)
		if Form.is_valid():
			Form.save()
			return redirect('Producto:ListaBanco')
			
		else:
			print('Error datos invalidos')
	contexto = {
		'Form':Form
	}
	return render(request, 'Productos/MetodoFormulario.html', contexto)
 
@login_required(login_url = 'Login:Login' )
def ListaMetodo(request):
	Lista = Metodo.objects.all()
	contexto={
		'Lista':Lista,
	}
	return render(request , 'Productos/MetodoLista.html', contexto)