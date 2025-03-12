from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class AthleteManager(BaseUserManager):
    """Manager for Athlete model"""
    
    def create_user(self, email, username, password=None, **extra_fields):
        """Create and return a regular athlete with an email and password"""
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """Create and return a superuser with an email, username, and password"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)

class Athlete(AbstractBaseUser):
    GENDER = [
        ("MALE", "Male"),
        ("FEMALE", "Female")
    ]

    athleteID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=6, choices=GENDER)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    biography = models.CharField(max_length=1000)
    smLinks = models.URLField(max_length=500)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    password = models.CharField(max_length=128, default='helloworld1')
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # True if the athlete is a staff (admin)
    
    # Add necessary fields for authentication
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # Email and username are required, but password is not (handled by AbstractBaseUser)

    objects = AthleteManager()

    def __str__(self):
        return f"Athlete: {self.username}"  # Displays the athlete's name
    
    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

class Event(models.Model):
    EVENTS = [
        ("60M", "60 Meters"),
        ("80M", "80 Meters"),
        ("100M", "100 Meters"),
        ("200M", "200 Meters"),
        ("400M", "400 Meters"),
        ("800M", "800 Meters"),
        ("1000M", "1000 Meters"),
        ("1200M", "1200 Meters"),
        ("1500M", "1500 Meters"),
        ("3000M", "3000 Meters"),
        ("5000M", "5000 Meters"),
        ("10000M", "10000 Meters"),
        ("60H", "60 Hurdles"),
        ("100H", "100 Hurdles"),
        ("110H", "110 Hurdles"),
        ("400H", "400 Hurdles"),
        ("3000SC", "3000 SC"),
        ("4100R", "4×100 Relay"),
        ("4400R", "4×400 Relay"),
        ("HM", "Half Marathon"),
        ("M", "Marathon"),
        ("20KW", "20K Walk"),
        ("PENT", "Pentathlon"),
        ("HEPT", "Heptathlon"),
        ("OCTA", "Octathlon"),
        ("DECA", "Decathlon"),
        ("HJ", "High Jump"),
        ("LJ", "Long Jump"),
        ("TRJ", "Triple Jump"),
        ("PV", "Pole Vault"),
        ("DISCUS", "Discus"),
        ("JAVE", "Javelin"),
        ("HAM", "Hammer"),
        ("SHOT", "Shot Put"),
        ("80H", "80 Hurdles"),
        ("BT", "Ball Throw"),
    ]

    eventID = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=200, choices=EVENTS)
    description = models.TextField(blank=True, null=True)  # Optional event description

    def __str__(self):
        return self.eventName  # Displays the event's name

class Match(models.Model):
    AGES = [
        ("OPEN", "Open"),
        ("U-23", "Under-23"),
        ("U-20", "Under-20"),
        ("U-18", "Under-18"),
        ("U-17", "Under-17"),
        ("U-15", "Under-15"),
        ("U-13", "Under-13"),
        ("U-11", "Under-11"),
        ("U-09", "Under-9"),
    ]

    SEASON = [
        (2025, "2025"),
        (2024, "2024"),
        (2023, "2023"),
        (2022, "2022"),
        (2021, "2021"),
        (2020, "2020"),
        (2019, "2019"),
    ]

    matchID = models.AutoField(primary_key=True)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name="matches", null=True)  # ForeignKey to Athlete
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="matches", null=True)  # ForeignKey to Event
    windSpeed = models.DecimalField(max_digits=3, decimal_places=1)
    place = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    mark = models.CharField(max_length=10)
    age = models.CharField(max_length=5, choices=AGES)
    club = models.CharField(max_length=200, default=None, blank=True, null=True)  # The club name the athlete performed under for a match
    personalBest = models.DecimalField(max_digits=10, decimal_places=2)
    season = models.IntegerField(choices=SEASON)
    gender = models.CharField(max_length=6, choices=Athlete.GENDER, default="MALE")  # Match gender (can be different from athlete)

    def __str__(self):
        athlete_name = self.athlete.name if self.athlete else "No Athlete"
        event_name = self.event.eventName if self.event else "No Event"
        return f"Match: {athlete_name} - {event_name}"
