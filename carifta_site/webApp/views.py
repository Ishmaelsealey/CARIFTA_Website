from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Match, Event, Athlete
from .forms import MatchForm, SignupForm
from django.contrib.auth import get_user_model

# Create your views here. each function is a different view/screen

# View for Athlete Login
def athlete_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        athlete = authenticate(request, username=username, password=password)
        
        if athlete is not None:
            login(request, athlete)
            return redirect('athlete_matches')  # Redirect to athlete's match list page
        else:
            return render(request, 'website/login.html', {'error': 'Invalid credentials'})

    return render(request, 'website/login.html')

# View for Athlete Account Creation
def athlete_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            if password1 == password2:
                user = get_user_model().objects.create_user(
                    email=email,
                    username=username,
                    password=password1
                )
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'website/signup.html', {'error': 'Passwords do not match'})
    else:
        form = SignupForm()
    return render(request, 'website/signup.html', {'form': form})

# matches table function

def event_list(request):
    matches = Match.objects.all()
    athletes = Athlete.objects.all()

    # Get filter values from request
    age_filter = request.GET.get('age', '')
    gender_filter = request.GET.get('gender', '')
    season_filter = request.GET.get('season', '')
    event_filter = request.GET.get('event', '')
    athlete_search = request.GET.get('athlete', '')

    # Apply filters if they exist
    if age_filter:
        matches = matches.filter(age=age_filter)
    if gender_filter:
        matches = matches.filter(gender=gender_filter)
    if season_filter:
        matches = matches.filter(season=season_filter)
    if event_filter:
        matches = matches.filter(eventName=event_filter)
    if athlete_search:
        matches = matches.filter(athlete__name__icontains=athlete_search)

    # Context to pass to the template
    context = {
        'matches': matches,
        'athletes': athletes,
        'age_filter': age_filter,
        'gender_filter': gender_filter,
        'season_filter': season_filter,
        'event_filter': event_filter,
        'athlete_search': athlete_search,
        'age_choices': Match.AGES,  # Get all age choices
        'event_choices': Event.EVENTS,  # Get all event choices
        'season_choices': Match.SEASON,  # Get all season choices
    }

    return render(request, 'website/event_list.html', context)

# Athlete Matches function

@login_required
def athlete_matches(request):
  # Get the athlete's matches
	athlete = request.user.athlete  # Assuming the user model has a related 'athlete'
	matches = Match.objects.filter(athlete=athlete)

	# Add a match
	if request.method == 'POST':
		form = MatchForm(request.POST)
		if form.is_valid():
			# Associate the logged-in athlete with the new match
			new_match = form.save(commit=False)
			new_match.athlete = athlete  # Set the logged-in athlete
			new_match.save()
			return redirect('athlete_matches')  # Redirect back to the matches page
	else:
		form = MatchForm()

	return render(request, 'website/athlete_matches.html', {'matches': matches, 'form': form})