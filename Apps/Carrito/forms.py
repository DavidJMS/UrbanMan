from django import forms
## models form 
from Apps.Carrito.models import Factura , Metodo
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select

class FormularioPago(forms.ModelForm):
    class Meta:
        model  = Factura
        fields = [
        'NumeroReferenia',
        'BancoPago',
        'Nombre',  
        'Apellido',
        'Dni',
        'DireccionEnvio',
        'FechaPago'
        ]
        labels = {
        'NumeroReferenia':'Código De Referencia',
        'BancoPago':'Banco De Pago',
        'Nombre' : 'Nombre',
        'Apellido':'Apellido',
        'Dni':'DNI',
        'DireccionEnvio':'Dirección De Envío',
        'FechaPago':'Fecha De Pago',
        }
        widgets = {
        'Nombre': TextInput(attrs={'class':'form-control', 
              'required':'False',
              'disabled':False,
              'autocomplete':'off',
               'placeholder':'Nombre'}),
        'Apellido': TextInput(attrs={'class':'form-control', 
              'required':'False',
              'disabled':False,
              'autocomplete':'off',
               'placeholder':'Apellido'}),
        'Dni': TextInput(attrs={'class':'form-control', 
              'required':'False',
              'disabled':False,
              'autocomplete':'off',
               'placeholder':'DNI'}),
        'BancoPago': TextInput(attrs={'class':'form-control', 
              'required':'False',
              'disabled':False,
              'autocomplete':'off',
               'placeholder':'Banco De Pago'}),
        'NumeroReferenia': TextInput(attrs={'class':'form-control', 
              'required':'False',
              'disabled':False,
              'autocomplete':'off',
               'placeholder':'Código De Referencia'}),
        'DireccionEnvio': TextInput(attrs={'class':'form-control', 
              'required':'False',
              'disabled':False,
              'autocomplete':'off',
               'placeholder':'Dirección De Envío'}),
        'FechaPago': DateInput(attrs={'class':'form-control', 
              'required':'False',
              'disabled':False,
              'autocomplete':'off',
              'placeholder':'DD/MM/AAAA'}), }


class FormularioMetodo(forms.ModelForm):
  class Meta:
    model = Metodo
    fields = [
    'Nombre',
    'NumeroCuenta',
    'Banco',  
    'Dni',
    'Cuenta'
    ]
    labels = {
    'Nombre':'Nombre',
    'NumeroCuenta':'Numero De Cuenta',
    'Banco' : 'Banco',
    'Dni':'DNI o RIF',
    'Cuenta':'Tipo De Cuenta',
    }
    widgets = {
    'Nombre': TextInput(attrs={'class':'form-control', 
          'required':'False',
          'disabled':False,
          'autocomplete':'off',
          'placeholder':'Nombre'}),
    'NumeroCuenta': TextInput(attrs={'class':'form-control', 
          'required':'False',
          'disabled':False,
          'autocomplete':'off',
          'placeholder':'Numero De Cuenta'}),
    'Banco': TextInput(attrs={'class':'form-control', 
          'required':'False',
          'disabled':False,
          'autocomplete':'off',
          'placeholder':'Banco'}),
    'Dni': TextInput(attrs={'class':'form-control', 
          'required':'False',
          'disabled':False,
          'autocomplete':'off',
          'placeholder':'DNI o RIF'}),
    'Cuenta': TextInput(attrs={'class':'form-control', 
          'required':'False',
          'disabled':False,
          'autocomplete':'off',
          'placeholder':'Tipo De Cuenta'}),}