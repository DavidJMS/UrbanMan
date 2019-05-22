from django.db import models
from django.conf import settings
from datetime import datetime
# Create your models here.
class CompraTemporal(models.Model):
	NumeroReferenia = models.CharField(max_length=100,null=True,default='Ninguno')
	Usuario     = models.CharField(max_length=30,null=True,default='Ninguno')
	Nombre      = models.CharField(max_length=30,null=True,default='Ninguno')
	Descripcion =  models.CharField(max_length=30,null=True,default='Ninguno')
	Precio				= models.CharField(max_length=30,null=True,default='Ninguno')
	Estado		   = models.CharField(max_length=30,null=True,default='SinPagar')
	CodigoFactura     = models.CharField(max_length=30,null=True,default='Ninguna')

class CompraRelalizada(models.Model): 
	id2 			= models.CharField(max_length=100,null=True,default='Ninguno')
	NumeroReferenia = models.CharField(max_length=100,null=True,default='Ninguno')
	Usuario     = models.CharField(max_length=30,null=True,default='Ninguno')
	Nombre      = models.CharField(max_length=30,null=True,default='Ninguno')
	Descripcion =  models.CharField(max_length=30,null=True,default='Ninguno')
	Precio		= models.CharField(max_length=30,null=True,default='Ninguno')
	Estado		    = models.CharField(max_length=30,null=True,default='SinPagar')
	CodigoFactura     = models.CharField(max_length=30,null=True,default='Ninguna')
	FechaPago       = models.DateField(default='AAAA-MM-DD', blank=False)

class Factura(models.Model):
	Usuario			= models.CharField(max_length=100,null=True,default='Ninguno')
	NumeroReferenia = models.CharField(max_length=100,null=True,default='Ninguno')
	BancoPago       = models.CharField(max_length=30,null=True,default='Ninguno')
	Nombre          = models.CharField(max_length=30,null=True,default='Ninguno')
	Apellido        = models.CharField(max_length=30,null=True,default='Ninguno')
	Dni             = models.CharField(max_length=30,null=True,default='Ninguno')
	DireccionEnvio 	= models.TextField(default='Dirección De Envío', null=True)
	FechaPago       = models.DateField(default='AAAA-MM-DD', blank=False)
	Verifiado = models.CharField(max_length=30,null=True,default='No')
	Monto       = models.CharField(max_length=30,null=True,default='Ninguno')

class Metodo(models.Model):
	Nombre			= models.CharField(max_length=30,null=True,default='Ninguno')
	NumeroCuenta	= models.CharField(max_length=100,null=True,default='Ninguno')
	Banco 			= models.CharField(max_length=30,null=True,default='Ninguno')
	Dni 			= models.CharField(max_length=30,null=True,default='Ninguno')
	Cuenta  		= models.CharField(max_length=30,null=True,default='Ninguno')
		