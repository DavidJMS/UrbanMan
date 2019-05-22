from django.conf.urls import url 
from Apps.Usuario.views import RegistroUsuario
urlpatterns = [
    
	url(r'^Registrar/$', RegistroUsuario.as_view() , name='Registrar'  ),	
]