from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from social.models import User, Dream

@csrf_exempt
def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('auth.html',{'state':state, 'username': username})


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
