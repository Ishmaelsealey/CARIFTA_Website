from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms

# Create your views here. each function is a different view/screen

# index function is used to show a specific file when it is called
def index(request):
	return render(request, 'website/index.html')

# login function

# return HttpResponse('Testing 123')


# user account function