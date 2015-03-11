from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery 
from social.models import Show, Dream


def home(request):
	return render(request, 'index.html', {})

def dream_info(request):
	return render(request, 'dreams.html', {'user_dreams' : Show.objects.all(),
                                               'dreams' : Dream.objects.all()
												 })

def flock_info(request):
	return render(request, 'flock.html', {})

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)
												 
def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	#empty string on the end basically means if you can't find some value at least return an invalid error
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('loggedin')
	else:
		return HttpResponseRedirect('invalid')

def loggedin(request):
	return render_to_response('loggedin.html', 
							 {'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')







###												 
##def bio(request):
##	actor_id = request.GET.get('id', None)
##	if not actor_id:
##		return home(request)
##	return render(request, 'bio.html', {'actor' : Actor.objects.filter(id=request.GET.get('id')).first()})
