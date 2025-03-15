from rest_framework import viewsets
from .models import Exercise, WorkoutDay
from .serializers import ExerciseSerializer, WorkoutDaySerializer



class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class WorkoutDayViewSet(viewsets.ModelViewSet):
    queryset = WorkoutDay.objects.all()
    serializer_class = WorkoutDaySerializer

    def get_queryset(self):
        # Obtener el queryset base
        queryset = super().get_queryset()
        
        # Obtener los parámetros de la URL
        day_of_week = self.request.query_params.get('day_of_week', None)
        start_date = self.request.query_params.get('start_date', None)

        # Filtrar por día de la semana (day_of_week)
        if day_of_week:
            queryset = queryset.filter(day_of_week__id=day_of_week)

        # Filtrar por fecha de inicio de la semana (start_date)
        if start_date:
            queryset = queryset.filter(workout_week__start_date=start_date)

        return queryset