"""Urban URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static  #importo static para que muestre las img 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^UrbanMan/', include('Apps.Man.urls', namespace='UrbanMan')),
    url(r'^Login/', include('Apps.Login.urls', namespace='Login')),
    url(r'^Producto/', include('Apps.Productos.urls', namespace='Producto')),
    url(r'^Usuario/', include('Apps.Usuario.urls', namespace='Usuario')),
    url(r'^Carrito/', include('Apps.Carrito.urls', namespace='Carrito')),    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #configuro mis rutas para que muestre las img
