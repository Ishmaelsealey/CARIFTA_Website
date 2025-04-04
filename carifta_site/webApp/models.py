from django.db import models
from django.contrib.auth.models import User

class AthleteProfile(models.Model):
    GENDER = [
        ("MALE", "Male"),
        ("FEMALE", "Female")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    gender = models.CharField(max_length=6, choices=GENDER)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    dob = models.DateField()
    biography = models.CharField(max_length=1000, blank=True, null=True)
    smLinks = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

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

    matchID = models.AutoField(primary_key=True)
    athlete = models.ForeignKey(AthleteProfile, on_delete=models.CASCADE, related_name="matches")
    event = models.CharField(max_length=20, choices=EVENTS, null=True)
    windSpeed = models.DecimalField(max_digits=3, decimal_places=1)
    place = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(blank=False)
    location = models.CharField(max_length=200)
    mark = models.CharField(max_length=10)
    age = models.CharField(max_length=5, choices=AGES)
    club = models.CharField(max_length=200, default=None, blank=True, null=True)
    personalBest = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    season = models.IntegerField(choices=SEASON)
    gender = models.CharField(max_length=6, choices=AthleteProfile.GENDER)

    def __str__(self):
        return f"Match: {self.athlete.name} - {self.event}"
