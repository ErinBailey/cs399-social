from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
#cross-site request forgery 
from social.models import User, Dream, UserForm, UserProfileForm
from django import forms


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



def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/dreams/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your MyStupidDreams account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})

												 
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
	#authenticate.logout(request)
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
                        print(user_form.errors, profile_form.errors)

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
