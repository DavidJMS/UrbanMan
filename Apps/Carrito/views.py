from django.shortcuts import render , redirect
from Apps.Carrito.models import CompraTemporal, CompraRelalizada , Factura
from django.db.models import Count, Min, Sum, Avg
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Apps.Carrito.forms import FormularioPago
from Apps.Carrito.models import Metodo
from django.core.mail import EmailMessage
# Create your views here.
@login_required(login_url = 'Login:Login' )
def VerCarritoTemporal(request):
	id_query= request.user.id
	ListaCompras= CompraTemporal.objects.filter(Usuario= id_query)
	contexto={
			'ListaCompras':ListaCompras,
			'total':'total',
			}
	return render(request,'Carrito/ListadeComprasTemporales.html',contexto)

@login_required(login_url = 'Login:Login' )
def NuevoPago(request):
    id_query= request.user.id
    ListaCompras= CompraTemporal.objects.filter(Usuario= id_query)
    Lista = Metodo.objects.all()
    Form = FormularioPago()
    if request.method == 'POST':
        Form  = FormularioPago(request.POST, request.FILES  or None)
        if Form.is_valid():
            Form.save()
            print(request.POST)
            query= CompraRelalizada.objects.filter(Estado= 'SinPagar')
            query.update(Estado='Pagado')
            query= CompraRelalizada.objects.filter(NumeroReferenia= 'Ninguno')
            query3 = Factura.objects.all().last()
            query3.Usuario = request.user.id
            query3.save()
            query.update(NumeroReferenia= query3.NumeroReferenia)
            query.update(CodigoFactura= query3.id)
            id_query= request.user.id
            query = CompraTemporal.objects.filter(Usuario= id_query)
            query.delete()
            asunto = 'Nuevo Registro De Compra, Numero De Referencia:'
            mensaje = query3
            mail = EmailMessage(asunto,mensaje, to=['david.marabay@gmail.com'])
            mail.send()
            return redirect('Carrito:Compras')
            
        else:
            print('Error datos invalidos')
    contexto = {
        'Form':Form,
        'ListaCompras':ListaCompras,
        'Lista':Lista,
    }
    return render(request, 'Carrito/NuevoPago.html', contexto)

@login_required(login_url = 'Login:Login' )
def ComprasRelalizada(request):
    id_query= request.user.id
    ListaCompras= CompraRelalizada.objects.filter(Usuario= id_query)
    ListaFactura= Factura.objects.filter(Usuario=id_query)
    contexto={
            'ListaCompras':ListaCompras,
            'ListaFactura':ListaFactura,
            }
    return render(request,'Carrito/ListadeComprasRealizadas.html',contexto)

@login_required(login_url = 'Login:Login' )
def EleminarArticulo(request):
    status = None
    id_Articulo = request.GET.get('id_Articulo', None)
    query  = CompraTemporal.objects.get( id = id_Articulo)
    query2 = CompraRelalizada.objects.filter(id2=id_Articulo, Estado='SinPagar')
    query.delete()
    query2.delete()
    status = 200
    return HttpResponse(status)

@login_required(login_url = 'Login:Login' )
def EleminarTodo(request):
    id_query= request.user.id
    query = CompraTemporal.objects.filter(Usuario= id_query)
    query2 = CompraRelalizada.objects.filter(Usuario=id_query, Estado='SinPagar')
    query.delete()
    query2.delete()
    return redirect('Carrito:Agregar')


@login_required(login_url = 'Login:Login' )
def ComprasRealizadas(request):
    ListaCompras= CompraRelalizada.objects.all()
    ListaFactura= Factura.objects.all()
    contexto={
            'ListaCompras':ListaCompras,
            'ListaFactura':ListaFactura,
            }
    return render(request,'Carrito/ListadeComprasRealizadas.html',contexto)