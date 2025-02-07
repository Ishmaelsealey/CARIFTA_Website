from django.urls import path

# imports the views.py file from the root of this directory
from . import views

urlpatterns = [
	# References the index function in the views.py file
	path("", views.index, name="index"),
]