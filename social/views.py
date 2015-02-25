from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse


def home(request):
	return render(request, 'index.html', {})
    



