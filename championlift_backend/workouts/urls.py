from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet, WorkoutDayViewSet

# router = DefaultRouter()
# router.register(r'exercises', ExerciseViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

router = DefaultRouter()
router.register(r'workoutdays', WorkoutDayViewSet)

urlpatterns = [
    path('', include(router.urls)),
]