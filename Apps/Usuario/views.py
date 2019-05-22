from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
# Create your views here.
class RegistroUsuario(CreateView):
	model = User
	template_name ="Usuario/Registro.html"
	form_class = UserCreationForm
	success_url = reverse_lazy('Producto:ListadeCategorias')
