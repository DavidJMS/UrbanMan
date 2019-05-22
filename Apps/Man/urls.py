from django.conf.urls import url 
from Apps.Man.views import Man
from Apps.Man.views import Contactanos
from Apps.Man.views import Productos
from Apps.Man.views import Tienda, TiendaCategoria, Busqueda
urlpatterns = [
    #url(r'^lista/$',listadeusuarios,name='listadeusuarios') , 
    url(r'^$',Man , name='Man' ),
    url(r'^Contactanos/$',Contactanos , name='Contactanos' ),
    url(r'^Productos/$',Productos , name='Productos' ),
    url(r'^Tienda/$',Tienda , name='Tienda' ),
    url(r'^Tienda/(?P<id_Categoria1>\d+)$',TiendaCategoria , name='TiendaCategoria' ),
    url(r'^Busqueda/$',Busqueda , name='Busqueda' ),
]