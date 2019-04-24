from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
# Create your views here.

@login_required(login_url = 'Login:Login' )
def Inicio(request):
	return render(request, 'Productos/Ropa.html')

def Login(request):
	if request.method == 'POST':
		usuario =  request.POST['usuario']
		password = request.POST['password']
		user = authenticate(username=usuario , password = password)
		if user is not None:
			login_django(request, user)
			return redirect('Login:Inicio')
		else:
			print('usuario invalido')
	return render(request, 'Login/Login.html')


@login_required(login_url = 'Login:Login' )
def Logout(request):
	logout_django(request)
	return redirect('Login:Login')