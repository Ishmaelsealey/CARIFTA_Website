from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Match, AthleteProfile
from .forms import MatchForm, SignupForm

# View for User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('athlete_matches')  # Redirect to match list page
        else:
            return render(request, 'website/login.html', {'error': 'Invalid credentials'})

    return render(request, 'website/login.html')

# View for User Signup
def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('athlete_matches')

    else:
        form = SignupForm()

    return render(request, 'website/signup.html', {"form": form})

# Matches table function
def event_list(request):
    matches = Match.objects.all()
    users = User.objects.all()

    # Get filter values from request
    age_filter = request.GET.get('age', '')
    gender_filter = request.GET.get('gender', '')
    season_filter = request.GET.get('season', '')
    event_filter = request.GET.get('event', '')
    athlete_search = request.GET.get('athlete', '')

    # Apply filters
    if age_filter:
        matches = matches.filter(age=age_filter)
    if gender_filter:
        matches = matches.filter(gender=gender_filter)
    if season_filter:
        matches = matches.filter(season=season_filter)
    if event_filter:
        matches = matches.filter(event__eventName=event_filter)
    if athlete_search:
        matches = matches.filter(athlete__username__icontains=athlete_search)

    context = {
        'matches': matches,
        'users': users,
        'age_filter': age_filter,
        'gender_filter': gender_filter,
        'season_filter': season_filter,
        'event_filter': event_filter,
        'athlete_search': athlete_search,
        'age_choices': Match.AGES,
        'event_choices': Match.EVENTS,
        'season_choices': Match.SEASON,
    }

    return render(request, 'website/event_list.html', context)

# Athlete Matches function
@login_required
def athlete_matches(request):
    user = request.user

    try:
        athlete = AthleteProfile.objects.get(user=user)
    except AthleteProfile.DoesNotExist:
        athlete = None
    
    matches = Match.objects.filter(athlete=athlete)

    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            new_match = form.save(commit=False)
            new_match.athlete = athlete
            new_match.gender = athlete.gender
            new_match.save()
            return redirect('athlete_matches')

    else:
        form = MatchForm()

    return render(request, 'website/athlete_matches.html', {'matches': matches, 'form': form, 'athlete': athlete})

def logout_view(request):
    logout(request)
    return redirect('login')
