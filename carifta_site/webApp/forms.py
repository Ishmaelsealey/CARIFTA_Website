from django import forms
from .models import Match, Athlete

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['event', 'age', 'season', 'mark', 'windSpeed', 'place', 'club', 'date', 'location', 'personalBest']

class SignupForm(forms.ModelForm):
    # Required fields are already specified in the model (username, email, etc.)
    # We will just make sure that the `biography` and `smLinks` are not mandatory.

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = Athlete
        fields = [
            'username', 'email', 'gender', 'weight', 'height', 'dob', 
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
