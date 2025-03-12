from django.urls import path

# imports the views.py file from the root of this directory
from . import views

urlpatterns = [
	path('events/', views.event_list, name='event_list'),
	path('athlete/matches/', views.athlete_matches, name='athlete_matches'),
	path('login/', views.athlete_login, name='login'),
	path('signup/', views.athlete_signup, name='signup'),
	path('logout/', views.logout_view, name='logout'),
]