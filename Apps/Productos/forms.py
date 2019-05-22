from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
## models form 
from Apps.Productos.models import Categoria,Producto
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select

class FormularioCategoria(forms.ModelForm):
	class Meta:
		model  = Categoria
		fields = [
		'Nombre',
		]
		labels = {
		'Nombre':'Nombre',
		'FechadeCreacion':'Fecha De Creacion',
		'FechadeModificacion' : 'Fecha De Modificacion',
		}
		widgets = {
		'Nombre': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Nombre De La Categoria'}),
		}

class FormularioProducto(forms.ModelForm):
	class Meta:
		model  = Producto
		fields = [
		'Categoria',
		'Nombre',
		'Categoria1',
		'Precio',
		'Existencia',
		'Referencia',
		'descripcion',
		'Imagen',
		]
		labels = {
		'Categoria':'Categoria Del Producto',
		'Nombre':'Nombre',
		'Categoria1':'Nombre De La Categoria',
		'Precio':'Precio Del Producto',
		'Existencia':'Existencia Del Producto',
		'Referencia':'Referencia Del Producto',
		'descripcion':'Descripcion Del Producto',
		'Imagen':'Imagen Del Producto',
		}
		widgets = {
		'Categoria1': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Nombre De La Categoria'}),
		'Nombre': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Nombre Del Producto'}),
		'Precio': NumberInput(
					attrs={
						'class':'form-control',
						'required':'False',
						'autocomplete':'off',
						'placeholder':'Precio Del Producto'}),
		'Existencia': NumberInput(
					attrs={
						'class':'form-control',
						'required':'False',
						'autocomplete':'off',
						'placeholder':'Existencia Del Producto'}),
		'Referencia': TextInput(
					attrs={
						'class':'form-control',
						'required':'False',
						'autocomplete':'off',
						'placeholder':'Referencia Del Producto'}),
		'descripcion': TextInput(
					attrs={
						'class':'form-control',
						'required':'False',
						'autocomplete':'off',
						'placeholder':'Descripcion Del Producto'}),
		'Imagen': FileInput(
					attrs={
						'class':'form-control',
						'required':'False',
						'autocomplete':'off',
						'placeholder':'Imagen Del Producto'}),
		}
