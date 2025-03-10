from django.db import models

# Create your models here.

class Athlete(models.Model):
	GENDER = [
		("MALE", "Male"),
		("FEMALE", "Female")
	]

	athleteID = models.AutoField(primary_key=True)
	name = models.CharField(max_length= 100)
	email = models.EmailField(max_length=200)
	gender = models.CharField(max_length=6, choices=GENDER)
	weight = models.DecimalField(max_digits=6, decimal_places=2)
	biography = models.CharField(max_length=1000)
	smLinks = models.URLField(max_length=500)
	height = models.DecimalField(max_digits=4, decimal_places=2)
	dob = models.DateField(auto_now=False,auto_now_add=False)
	# matches = models.ForeignKey(Match, on_delete=models.CASCADE)

	def __str__(self):
		return f"Athlete: {self.name}"  # Displays the athlete's name

class Match(models.Model):
	AGES = [
		("OPEN", "Open"),
		("U-17", "Under-17"),
		("U-15", "Under-15"),
		("U-13", "Under-13"),
		("U-11", "Under-11"),
		("U-09", "Under-9"),
	]

	EVENTS = [
		("60", "60"),
		("100", "100"),
		("200", "200"),
		("400", "400"),
		("800", "800"),
		("1500", "1500"),
		("3000", "3000"),
		("5000", "5000"),
		("10000", "10000"),
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
		("80", "80 Metres"),
		("1000", "1000 Metres"),
		("1200", "1200 Metres"),
		("80H", "80 Hurdles"),
		("BT", "Ball Throw"),
	]
	
	GENDER = [
		("MALE", "Male"),
		("FEMALE", "Female")
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
	windSpeed = models.DecimalField(max_digits=6, decimal_places=3)
	place = models.CharField(max_length=200)
	club = models.CharField(max_length=200)
	date = models.DateField(auto_now=False, auto_now_add=False)
	location = models.CharField(max_length=200)
	eventName = models.CharField(max_length=200, choices=EVENTS)
	season = models.IntegerField(choices=SEASON)
	mark = models.CharField(max_length=10)
	age = models.CharField(max_length=5, choices=AGES)
	personalBest = models.DecimalField(max_digits=10, decimal_places=2)
	gender = models.CharField(max_length=6, choices=GENDER, default="MALE")

	def __str__(self):
		return f"Event: {self.eventName}"  # Displays the event's name
		
class Coach(models.Model):
	GENDER = [
		("MALE", "Male"),
		("FEMALE", "Female")
	]

	coachID = models.AutoField(primary_key=True)
	name = models.CharField(max_length= 100)
	email = models.EmailField(max_length=200)
	gender = models.CharField(max_length=6, choices=GENDER)

	def __str__(self):
		return f"Coach: {self.name}"  # Displays the coach's name
