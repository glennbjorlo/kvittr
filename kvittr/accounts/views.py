from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import UpdatePicture

# Create your views here.

def userregister(request):
	context = {}
	if request.method == 'POST':
		user = User()
		user.first_name = request.POST.get('firstname')
		user.last_name = request.POST.get('lastname')
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


def updateprofile(request):
	if request.method == 'POST':
		userprofile = User.objects.get(username=request.user)
		userprofile.first_name = request.POST.get('updatefirstname')
		userprofile.last_name = request.POST.get('updatelastname')
		userprofile.email = request.POST.get('updateemail')
		userprofile.save()
	return render(request, 'accounts/usersettings.html')


def uploadpic(request):
	if request.method == 'POST':
		userimage = UpdatePicture()
		userimage.uname = request.user
		userimage.user_picture = request.POST.get('profilepicture')
		userimage.save()
	allimages = UpdatePicture.objects.all()
	return render(request, 'accounts/pic.html')
	













	
