from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    rep_range_min = models.PositiveIntegerField()
    rep_range_max = models.PositiveIntegerField()
    weight_min = models.DecimalField(max_digits=5, decimal_places=2)
    weight_max = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class WeekDay(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class WorkoutWeek(models.Model):
    start_date = models.DateField()
    exercises = models.ManyToManyField(Exercise, through='WorkoutDay')

    def __str__(self):
        return f"Workout Week starting {self.start_date}"


class WorkoutDay(models.Model):
    workout_week = models.ForeignKey(WorkoutWeek, related_name='workout_days', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, related_name='workout_days', on_delete=models.CASCADE)
    day_of_week = models.ForeignKey(WeekDay, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.exercise} on {self.day_of_week} in week starting {self.workout_week.start_date}"

