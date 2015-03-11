from django.shortcuts import render
from django.http import HttpResponse
from social.models import User, Dream


def home(request):
	return render(request, 'index.html', {})

def dream_info(request):
	return render(request, 'dreams.html', {'user_dreams' : User.objects.all(),
                                               'dreams' : Dream.objects.all()
												 })

def flock_info(request):
	return render(request, 'flock.html', {})

def about(request):
	return render(request, 'about.html', {})

def login(request):
	return render(request, 'login.html', {'user_login' : User.objects.all(),
												 })

def logout(request):
	return render(request, 'logout.html', {'logout' : Dream.objects.all(),
												 })
###												 
##def bio(request):
##	actor_id = request.GET.get('id', None)
##	if not actor_id:
##		return home(request)
##	return render(request, 'bio.html', {'actor' : Actor.objects.filter(id=request.GET.get('id')).first()})
