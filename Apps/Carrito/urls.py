from django.conf.urls import url 
from Apps.Carrito.views import VerCarritoTemporal, NuevoPago
from Apps.Carrito.views import ComprasRelalizada, EleminarArticulo, EleminarTodo, ComprasRealizadas
urlpatterns = [
	url(r'^Agregar/$', VerCarritoTemporal , name='Agregar'  ),	
    url(r'^Pagar/$', NuevoPago , name='Pagar'  ),
    url(r'^Compras/$', ComprasRelalizada , name='Compras'  ),
    url(r'^Eliminar/$', EleminarArticulo	 , name='Eliminar'  ),
    url(r'^EliminarTodo/$', EleminarTodo	 , name='EliminarTodo'  ),
    url(r'^ComprasAdministrador/$', ComprasRealizadas	 , name='ComprasAdministrador'  ),
]