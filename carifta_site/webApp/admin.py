from django.contrib import admin
from.models import AthleteProfile, Match, Event

# Register your models here.

admin.site.register(AthleteProfile)
admin.site.register(Event)
admin.site.register(Match)