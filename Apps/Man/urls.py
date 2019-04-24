from django.conf.urls import url 
from Apps.Man.views import Man
from Apps.Man.views import Contactanos
from Apps.Man.views import Productos
urlpatterns = [
    #url(r'^lista/$',listadeusuarios,name='listadeusuarios') , 
    url(r'^$',Man , name='Man' ),
    url(r'^Contactanos/$',Contactanos , name='Contactanos' ),
    url(r'^Productos/$',Productos , name='Productos' ),
]