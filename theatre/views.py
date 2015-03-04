from django.shortcuts import render
from django.http import HttpResponse
from theatre.models import Show, Actor, Seat, Information


def home(request):
	return render(request, 'index.html', {})

def information_performance(request):
	return render(request, 'dreams.html', {'performances' : Show.objects.all(),
												 'actors' : Actor.objects.all()})

def merchandise(request):
	return render(request, 'flock.html', {})

def performances(request):
	return render(request, 'login.html', {'performances' : Show.objects.all(),
												 'actors' : Actor.objects.all()})

def ticket_sales(request):
	return render(request, 'logout.html', {'performances' : Show.objects.all(),
												 'actors' : Actor.objects.all(),
												 'ticket_sales' : Seat.objects.all()})
												 
def bio(request):
	actor_id = request.GET.get('id', None)
	if not actor_id:
		return home(request)
	return render(request, 'bio.html', {'actor' : Actor.objects.filter(id=request.GET.get('id')).first()})
