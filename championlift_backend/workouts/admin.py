from django.contrib import admin
from .models import Exercise, WeekDay, WorkoutDay, WorkoutWeek

# Register your models here.
admin.site.register(Exercise)
admin.site.register(WeekDay)
admin.site.register(WorkoutWeek)
admin.site.register(WorkoutDay)
