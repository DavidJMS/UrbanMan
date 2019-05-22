from Apps.Carrito.models import CompraTemporal
from django.db.models import Count, Min, Sum, Avg

def Total(request):
	id_query= request.user.id
	Total = CompraTemporal.objects.filter(Usuario= id_query).aggregate(total=Sum('Precio'))
	if (Total['total'] == None):
		Total['total'] = 0
	return {'Total':Total}
