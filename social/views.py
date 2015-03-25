from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
#cross-site request forgery 
from social.models import User, Dream, UserForm, UserProfileForm


def home(request):
	return render(request, 'index.html', {})

def dream_info(request):
	return render(request, 'dreams.html', {'user_dreams' : User.objects.all(),
                                               'dreams' : Dream.objects.all()
												 })

def flock_info(request):
	return render(request, 'flock.html', {'user_dreams' : User.objects.all(), 'dreams' : Dream.objects.all(),
                                               'flocks' : Dream.objects.values('flock').distinct()})


def about(request):
	return render(request, 'about.html', {})

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


def register(request):
        registered = False
        if request.method == 'POST':
                user_form = UserForm(data=request.POST)
                profile_form = UserProfileForm(data=request.POST)

                if user_form.is_valid() and profile_form.is_valid():
                        user = user_form.save()
                        user.set_password(user.password)
                        user.save()
                        
                        profile = profile_form.save(commit=False)
                        profile.user = user

                        if 'picture' in request.FILES:
                                profile.picture = request.FILES['picture']

                        profile.save()

                        registered = True

                else:
                        print user_form.errors, profile_form.errors

        else:
                user_form = UserForm()
                profile_form = UserProfileForm()

        return render(request,
                      'register.html',
                      {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

                        
                        

                




###												 
##def bio(request):
##	actor_id = request.GET.get('id', None)
##	if not actor_id:
##		return home(request)
##	return render(request, 'bio.html', {'actor' : Actor.objects.filter(id=request.GET.get('id')).first()})
