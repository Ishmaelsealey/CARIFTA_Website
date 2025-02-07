from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. each function is a different view/screen

# index function is used to show a specific screen when it is called
def index(request):
	return HttpResponse("Hello world!")