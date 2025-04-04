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
        matches = matches.filter(event=event_filter)
    if athlete_search:
        matches = matches.filter(athlete__name__icontains=athlete_search)

    # Sort matches based on event type (assume you have a way to determine event type)
    event_types = {
        # Sprint races - lower is better
        "60M": "ascending",
        "80M": "ascending",
        "100M": "ascending",
        "200M": "ascending",
        "400M": "ascending",
        "800M": "ascending",
        "1000M": "ascending",
        "1200M": "ascending",
        "1500M": "ascending",
        "3000M": "ascending",
        "5000M": "ascending",
        "10000M": "ascending",
        
        # Hurdles - lower is better
        "60H": "ascending",
        "80H": "ascending",
        "100H": "ascending",
        "110H": "ascending",
        "400H": "ascending",
        
        # Steeplechase - lower is better
        "3000SC": "ascending",
        
        # Relays - lower is better
        "4100R": "ascending",
        "4400R": "ascending",
        
        # Long-distance races - lower is better
        "HM": "ascending",   # Half Marathon
        "M": "ascending",    # Marathon

        # Walk races - lower is better
        "20KW": "ascending",
        
        # Combined events - higher is better
        "PENT": "descending",  # Pentathlon
        "HEPT": "descending",  # Heptathlon
        "OCTA": "descending",  # Octathlon
        "DECA": "descending",  # Decathlon

        # Jumping events - higher is better
        "HJ": "descending",  # High Jump
        "LJ": "descending",  # Long Jump
        "TRJ": "descending", # Triple Jump
        "PV": "descending",  # Pole Vault

        # Throwing events - higher is better
        "DISCUS": "descending",
        "JAVE": "descending",  # Javelin
        "HAM": "descending",   # Hammer
        "SHOT": "descending",  # Shot Put
        "BT": "descending",    # Ball Throw
    }

    if event_filter and event_filter in event_types:
        if event_types[event_filter] == "ascending":
            matches = matches.order_by("mark")  # Lower is better (race times)
        else:
            matches = matches.order_by("-mark")  # Higher is better (jump distances, throws)

    # Assign ranks based on sorted order
    ranked_matches = []
    previous_mark = None
    rank = 0

    for i, match in enumerate(matches):
        if previous_mark != match.mark:
            rank = i + 1  # Assign new rank if performance differs
        previous_mark = match.mark
        match.rank = rank  # Attach rank dynamically
        ranked_matches.append(match)

    context = {
        'matches': ranked_matches,
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
