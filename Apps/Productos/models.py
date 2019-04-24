from django.db import models
from django.conf import settings
from datetime import datetime
# Create your models here.
class Categoria(models.Model):
	Nombre      = models.CharField(max_length=20,null=True,default='Ninguno')
	FechadeCreacion =  models.DateTimeField(default=datetime.now, blank=True) 
	FechadeModificacion = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.Nombre

class Producto(models.Model):
	Categoria   = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, default='Sin Categoria')
	Nombre   	= models.CharField(max_length=15, null=True, default='Ninguno')
	Precio		= models.FloatField(default='0.0',null=True,)
	Existencia	= models.IntegerField(null=True, default=1)
	Referencia	= models.CharField(max_length=15, null=True, default='Ninguna')
	descripcion = models.CharField(max_length=30, null=True, default='Ninguna')
	Imagen		= models.ImageField(upload_to='Productos/Imagenes/', default='', null=True)
	FechadeCreacion =  models.DateTimeField(default=datetime.now, blank=True) 
	FechadeModificacion = models.DateTimeField(default=datetime.now, blank=True)  