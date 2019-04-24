from django import forms
## models form 
from Apps.Productos.models import Categoria,Producto
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select

class FormularioCategoria(forms.ModelForm):
	class Meta:
		model  = Categoria
		fields = [
		'Nombre',
		'FechadeCreacion',
		'FechadeModificacion',
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

		'FechadeCreacion': DateInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Fecha De Creacion'}),

		'FechadeModificacion': DateInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Fecha De Modificacion'}),
		}

class FormularioProducto(forms.ModelForm):
	class Meta:
		model  = Producto
		fields = [
		'Categoria',
		'Nombre',
		'Precio',
		'Existencia',
		'Referencia',
		'descripcion',
		'Imagen',
		'FechadeCreacion',
		'FechadeModificacion',
		]
		labels = {
		'Categoria':'Categoria Del Producto',
		'Nombre':'Nombre',
		'Precio':'Precio Del Producto',
		'Existencia':'Existencia Del Producto',
		'Referencia':'Referencia Del Producto',
		'descripcion':'Descripcion Del Producto',
		'Imagen':'Imagen Del Producto',
		'FechadeCreacion':'Fecha De Creacion',
		'FechadeModificacion' : 'Fecha De Modificacion',
		}
		widgets = {
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
		'FechadeCreacion': DateInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Fecha De Creacion'}),
		'FechadeModificacion': DateInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Fecha De Modificacion'}),
		}
