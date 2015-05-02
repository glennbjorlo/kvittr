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
