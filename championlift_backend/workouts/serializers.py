from rest_framework import serializers, status
from rest_framework.response import Response
from .models import Exercise, WorkoutDay, WorkoutWeek, WeekDay

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'sets', 'rep_range_min', 'rep_range_max', 'weight_min', 'weight_max']

class WeekDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekDay
        fields = ['id', 'name']

class WeekDayWithExercisesSerializer(serializers.ModelSerializer):
    exercises = serializers.SerializerMethodField()

    class Meta:
        model = WeekDay
        fields = ['id', 'name', 'exercises']

    def get_exercises(self, obj):
        workout_week = self.context.get('workout_week')
        if workout_week:
            workout_days = WorkoutDay.objects.filter(
                workout_week=workout_week,
                day_of_week=obj
            )
            exercises = [workout_day.exercise for workout_day in workout_days]
            return ExerciseSerializer(exercises, many=True).data
        return []

class WorkoutWeekSerializer(serializers.ModelSerializer):
    days_of_week = serializers.SerializerMethodField()

    class Meta:
        model = WorkoutWeek
        fields = ['id', 'start_date', 'days_of_week']

    def get_days_of_week(self, obj):
        week_days = WeekDay.objects.all()
        serializer = WeekDayWithExercisesSerializer(
            week_days, 
            many=True, 
            context={'workout_week': obj}
        )
        return serializer.data

# Este serializador lo mantenemos por si necesitas la vista plana en algún momento
class WorkoutDaySerializer(serializers.ModelSerializer):
    workout_week = WorkoutWeekSerializer()
    exercise = ExerciseSerializer()
    day_of_week = WeekDaySerializer()

    class Meta:
        model = WorkoutDay
        fields = ['id', 'workout_week', 'exercise', 'day_of_week']

    def create(self, validated_data):
        # Extraer los datos anidados
        workout_week_data = validated_data.pop('workout_week')
        exercise_data = validated_data.pop('exercise')
        day_of_week_data = validated_data.pop('day_of_week')

        # Crear o obtener el WorkoutWeek
        workout_week, _ = WorkoutWeek.objects.get_or_create(**workout_week_data)

        # Crear o obtener el Exercise
        exercise, _ = Exercise.objects.get_or_create(**exercise_data)

        # Crear o obtener el WeekDay
        day_of_week, _ = WeekDay.objects.get_or_create(**day_of_week_data)

        # Crear el WorkoutDay
        workout_day = WorkoutDay.objects.create(
            workout_week=workout_week,
            exercise=exercise,
            day_of_week=day_of_week,
            
        )

        return workout_day
    
    # def destroy(self, pk=None):
    #     try:
    #         usuario = self.queryset.get(pk=pk)  # self.get_object() también es una opción
    #         usuario.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)  # Sin contenido, eliminación exitosa
    #     except Usuario.DoesNotExist:
    #         return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    #     except Exception as e:
    #         return Response({'error': f'Error al eliminar el usuario: {str(e)}'},
    #                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)