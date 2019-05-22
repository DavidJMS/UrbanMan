from django.db import models
from datetime import datetime
# Create your models here.
class Categoria(models.Model):
	Nombre      = models.CharField(max_length=20,null=True,default='Ninguno')
	def __str__(self):
		return self.Nombre

class Producto(models.Model):
	Categoria   = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, default='Sin Categoria')
	Categoria1 = models.CharField(max_length=15, null=True, default='Ninguno')
	Nombre   	= models.CharField(max_length=15, null=True, default='Ninguno')
	Precio		= models.FloatField(default='0.0',null=True,)
	Existencia	= models.IntegerField(null=True, default=1)
	Referencia	= models.CharField(max_length=15, null=True, default='Ninguna')
	descripcion = models.CharField(max_length=30, null=True, default='Ninguna')
	Imagen		= models.ImageField(upload_to='Productos/Imagenes/', default='', null=True)
	