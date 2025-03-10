from django.contrib import admin
from.models import Athlete, Match, Event

# Register your models here.

admin.site.register(Athlete)
admin.site.register(Event)
admin.site.register(Match)