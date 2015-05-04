from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def userregister(request):
	context = {}
	if request.method == 'POST':
		user = User()
		user.firstname = request.POST.get('firstname')
		user.lastname = request.POST.get('lastname')
		user.username = request.POST.get('username')
		user.email = request.POST.get('email')
		user.set_password(request.POST.get('password'))
		user.save()
		context['user_saved_successfully'] = True
	return render(request, 'accounts/registration.html', context)
	

def userlogin(request):
	context = {}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('frontpage')
		else:
			context['login_failed'] = True
	return render(request, 'accounts/login.html', context)


def userlogout(request):
	logout(request)
	return redirect('frontpage')
