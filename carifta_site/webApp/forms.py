from django import forms
from .models import Match, Athlete

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
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'mark': forms.TextInput(attrs={'placeholder': 'Enter mark in seconds/meters'}),
            'windSpeed': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'Enter wind speed in m/s'}),
            'place': forms.TextInput(attrs={'placeholder': 'e.g., 1st, 2nd, 3rd'}),
            'club': forms.TextInput(attrs={'placeholder': 'Optional'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter event location'}),
            'personalBest': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'Enter best mark'}),
        }

class SignupForm(forms.ModelForm):
    # Required fields are already specified in the model (username, email, etc.)
    # We will just make sure that the `biography` and `smLinks` are not mandatory.

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = Athlete
        fields = [
            'name', 'email', 'username', 'gender', 'weight', 'height', 'dob', 
            'biography', 'smLinks'  # biography and smLinks are optional
        ]
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields must match.")
        return password2

    def save(self, commit=True):
        # Save the password correctly
        athlete = super().save(commit=False)
        athlete.set_password(self.cleaned_data["password1"])
        if commit:
            athlete.save()
        return athlete
