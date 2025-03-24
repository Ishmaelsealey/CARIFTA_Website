from django import forms
from django.contrib.auth.models import User
from .models import Match, AthleteProfile

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['event', 'age', 'season', 'mark', 'windSpeed', 'place', 'club', 'date', 'location', 'personalBest']

        labels = {
            'event': 'Select Event',
            'age': 'Select Age Category',
            'season': 'Season (Year)',
            'mark': 'Performance Mark (e.g., 10.25s, 5.50m)',
            'windSpeed': 'Wind Speed (m/s)',
            'place': 'Placement (e.g., 1st, 2nd, 3rd)',
            'club': 'Club Name (Optional)',
            'date': 'Date of Match (YYYY-MM-DD)',
            'location': 'Location of Event',
            'personalBest': 'Personal Best Performance',
        }

        widgets = {
            'event': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.Select(attrs={'class': 'form-control'}),
            'season': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'mark': forms.TextInput(attrs={'placeholder': 'Enter mark in seconds/meters', 'class': 'form-control'}),
            'windSpeed': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'Enter wind speed in m/s', 'class': 'form-control'}),
            'place': forms.TextInput(attrs={'placeholder': 'e.g., 1st, 2nd, 3rd', 'class': 'form-control'}),
            'club': forms.TextInput(attrs={'placeholder': 'Optional', 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter event location', 'class': 'form-control'}),
            'personalBest': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'Enter best mark', 'class': 'form-control'}),
        }

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    name = forms.CharField(label="Full Name", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=AthleteProfile.GENDER, widget=forms.Select(attrs={'class': 'form-control'}))
    weight = forms.DecimalField(label="Weight (kg)", max_digits=6, decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    height = forms.DecimalField(label="Height (m)", max_digits=4, decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dob = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    biography = forms.CharField(label="Biography", required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    smLinks = forms.URLField(label="Social Media Link", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields must match.")
        return password2

    def save(self, commit=True):
        """ 
        1. Save the user instance 
        2. Create and link the AthleteProfile to the user 
        """

        user = super().save(commit=False) # Don't commit yet, we need to set the password
        user.set_password(self.cleaned_data["password1"])
        
        if commit:
            user.save() # Save the User first so we can link it to AthleteProfile

            # Create the AthleteProfile and link it to user
            athlete_profile = AthleteProfile.objects.create(
                user=user,
                name=self.cleaned_data["name"],
                gender=self.cleaned_data["gender"],
                weight=self.cleaned_data["weight"],
                height=self.cleaned_data["height"],
                dob=self.cleaned_data["dob"],
                biography=self.cleaned_data["biography"],
                smLinks=self.cleaned_data["smLinks"]
            )
            athlete_profile.save() # ensure it's saved

        return user
