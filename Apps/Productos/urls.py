from django.conf.urls import url 
from Apps.Productos.views import NuevaCategoria
from Apps.Productos.views import NuevoProducto
from Apps.Productos.views import ListadeCategorias
from Apps.Productos.views import ListadeProductos
from Apps.Productos.views import EliminarCategoria
from Apps.Productos.views import EliminarProducto
from Apps.Productos.views import EditarCategoria
from Apps.Productos.views import EditarProducto
from Apps.Productos.views import DetalleProducto
from Apps.Productos.views import DetalleCategoria
urlpatterns = [
    url(r'^Categoria/Nueva$',NuevaCategoria , name='NuevaCategoria' ),
	url(r'^Producto/Nuevo$',NuevoProducto , name='NuevoProducto' ),
	url(r'^Categorias/Lista$',ListadeCategorias , name='ListadeCategorias' ),
	url(r'^Productos/Lista$',ListadeProductos , name='ListadeProductos' ),
	url(r'^EditarCategori(?P<id_Categoria1>\d+)$',EditarCategoria , name='EditarCategoria' ),
	url(r'^EditarProducto/(?P<id_Producto1>\d+)$',EditarProducto , name='EditarProducto' ),
	url(r'^Productos/Eliminar$',EliminarProducto , name='EliminarProducto' ),
	url(r'^Categoria/Eliminar$',EliminarCategoria , name='EliminarCategoria' ),
	url(r'^DetalleProducto/(?P<id_Producto>\d+)$', DetalleProducto , name='DetalleProducto'  ),	
	url(r'^DetalleCategoria/(?P<id_Categoria1>\d+)$', DetalleCategoria , name='DetalleCategoria'  ),	
]